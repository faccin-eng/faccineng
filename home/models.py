from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class TwoColumnBlock(blocks.StructBlock):
    background_image_left = ImageChooserBlock(required=False, label="Imagem de fundo (esquerda)")
    text_left = blocks.RichTextBlock(required=False, label="Texto (esquerda)")
    front_image_left = ImageChooserBlock(required=False, label="Imagem/ícone frontal (esquerda)")
    
    background_image_right = ImageChooserBlock(required=False, label="Imagem de fundo (direita)")
    text_right = blocks.RichTextBlock(required=False, label="Texto (direita)")
    front_image_right = ImageChooserBlock(required=False, label="Imagem/ícone frontal (direita)")
    
    class Meta:
        template = 'home/blocks/two_column_block.html'
        icon = 'grip'
        label = 'Duas colunas'


class HomePage(Page):
    body = StreamField([
        ('two_columns', TwoColumnBlock()),
        ('rich_text', blocks.RichTextBlock(label="Texto livre")),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]