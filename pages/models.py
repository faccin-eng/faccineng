from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel

class StandardPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
    ], use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]