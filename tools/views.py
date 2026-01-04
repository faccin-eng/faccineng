from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django_ratelimit.decorators import ratelimit
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from ofxparse import OfxParser
import csv
import io

MAX_FILE_SIZE = 5 * 1024 * 1024  

@ratelimit(key='ip', rate='6/h', method='POST')
class ofx_converter(Page):
    max_count = 1

    intro_text = RichTextField(
        blank = True,
        verbose_name="Texto de introdução",
        help_text="Texto explicativo da ferramenta"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
    ]
    def serve(self, request):
        if request.method == 'POST' and request.FILES.get('ofx_file'):
            ofx_file = request.FILES['ofx_file']
            
            if ofx_file.size > MAX_FILE_SIZE:
                return HttpResponseBadRequest("Arquivo muito grande (máx 5MB)")
            
            if not ofx_file.name.lower().endswith('.ofx'):
                return HttpResponseBadRequest("Apenas arquivos .ofx são permitidos")
            
            allowed_types = ['application/x-ofx', 'application/octet-stream', 'text/plain']
            if ofx_file.content_type not in allowed_types:
                return HttpResponseBadRequest("Tipo de arquivo inválido")
            
            try:
                ofx = OfxParser.parse(ofx_file)
                
                transactions = list(ofx.account.statement.transactions)
                if len(transactions) > 10000:
                    return HttpResponseBadRequest("Arquivo com muitas transações")
                
                output = io.StringIO()
                writer = csv.writer(output, delimiter=';')
                writer.writerow(['Data', 'Descrição', 'Valor'])
                
                for trans in transactions:
                    valor_formatado = f"{trans.amount:.2f}".replace('.', ',')
                    writer.writerow([
                        trans.date.strftime('%d/%m/%Y'),
                        trans.payee[:200], 
                        valor_formatado
                    ])
                
                response = HttpResponse(output.getvalue(), content_type='text/csv; charset=utf-8')
                response['Content-Disposition'] = 'attachment; filename="extrato.csv"'
                return response
                
            except Exception as e:
                print("ERRO:", str(e)) 
                return HttpResponseBadRequest("Erro ao processar arquivo")
        
        return render(request, 'tools/ofx_converter.html',{
            'page': self,
        })