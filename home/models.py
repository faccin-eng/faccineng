from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class ColumnContentBlock(blocks.StreamBlock):
    rich_text = blocks.RichTextBlock(label="Texto")
    image = ImageChooserBlock(label="Imagem")
    raw_html = blocks.RawHTMLBlock(label="HTML/Embed")
    class Meta:
        icon = 'placeholder'

class TwoColumnBlock(blocks.StructBlock):
    min_height = blocks.IntegerBlock(
        required=False,
        default=300,
        label="Altura mínima (px)",
        help_text="Defina a altura dos blocos"
    )
    background_image_left = ImageChooserBlock(required=False, label="Imagem de fundo (esquerda)")
    content_left = ColumnContentBlock(required=False, label="Conteúdo (esquerda)")
    
    background_image_right = ImageChooserBlock(required=False, label="Imagem de fundo (direita)")
    content_right = ColumnContentBlock(required=False, label="Conteúdo (direita)")
    
    class Meta:
        template = 'home/blocks/two_column_block.html'
        icon = 'grip'
        label = 'Duas colunas'

class FullWidthBlock(blocks.StructBlock):
    min_height = blocks.IntegerBlock(
        required=False,
        default=300,
        label="Altura mínima (px)",
        help_text="Defina a altura dos blocos"
    )
    background_image = ImageChooserBlock(required=False, label="Imagem de fundo")
    content = ColumnContentBlock(required=False, label="Conteúdo")

    class Meta:
        template = 'home/blocks/full_width_block.html'
        icon = 'horizontalrule'
        label = 'Bloco estendido'

class HomePage(Page):
    body = StreamField([
        ('two_columns', TwoColumnBlock()),
        ('full_width', FullWidthBlock()),
        ('rich_text', blocks.RichTextBlock(label="Texto livre")),
        ('raw_html', blocks.RawHTMLBlock(label="HTML/Embed grande")),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]