from django.shortcuts import render
from django.http import HttpResponse
from ofxparse import OfxParser
import csv
import io

def ofx_converter(request):
    if request.method == 'POST' and request.FILES.get('ofx_file'):
        print("POST recebido")
        
        if request.FILES.get('ofx_file'):
            ofx_file = request.FILES['ofx_file']
            print('arquivo recebido:', ofx_file.name)

            try:
                ofx = OfxParser.parse(ofx_file)
                print("parseado com sucesso")

                output = io.StringIO()
                writer = csv.writer(output, delimiter=';')
                writer.writerow(['Data', 'Descrição', 'Valor'])

            
                for trans in ofx.account.statement.transactions:
                    valor_formatado = f"{trans.amount:.2f}".replace('.',',')

                    writer.writerow([
                        trans.date.strftime('%d/%m/%Y'),
                        trans.payee,
                        valor_formatado
                    ])
                print("CSV gerado, tamanho:", len(output.getvalue()))

                response = HttpResponse(output.getvalue(),content_type='text/CSV; charset=utf-8')
                response['Content-Disposition'] = 'attachment; filename="converted.csv"'
                return response
            except Exception as e:
                print("ERRO:", str(e))
                import traceback
                traceback.print_exc()
    return render(request, 'tools/ofx_converter.html')