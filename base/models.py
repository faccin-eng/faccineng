from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.fields import RichTextField

from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.snippets.models import register_snippet

@register_setting
class FooterSettings(BaseGenericSetting):
    linkedin_url = models.URLField(verbose_name="Linkedin", blank=True)
    zap_url = models.URLField(verbose_name="What's App", help_text="(wa.me/+55seunumeroaqui)", blank=True)
    github_url = models.URLField(verbose_name="GitHub", blank=True)
    face_url = models.URLField(verbose_name="Facebook", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)

    banner_image1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Banner 1 (800x110px)"
    )
    
    banner_url1 = models.URLField(
        blank=True,
        verbose_name="Link Imagem 1",
        help_text="URL opcional da imagem 1)"
    )

    footer_text = RichTextField(blank=True, verbose_name="Texto do Rodapé")

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("linkedin_url"),
                FieldPanel("zap_url"),
                FieldPanel("github_url"),
                FieldPanel("face_url"),
                FieldPanel("instagram_url"),
            ], "Links das mídias sociais"),

        MultiFieldPanel([
            FieldPanel("banner_image1"),
            FieldPanel("banner_url1"),
        ], "Configurações do carrossel de banners do Rodapé (800x110px)"),
        FieldPanel("footer_text"),
    ]
@register_setting
class HeaderSettings(BaseGenericSetting):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Logo Cabeçalho"
    )
    favicon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Favicon'
    )
    banner_image1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Banner 1 (800x110px)"
    )
    banner_image2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Banner 2 (800x110px)"
    )
    banner_image3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Banner 3 (800x110px)"
    )
    
    banner_url1 = models.URLField(
        blank=True,
        verbose_name="Link Imagem 1",
        help_text="URL opcional da imagem 1)"
    )
    banner_url2 = models.URLField(
        blank=True,
        verbose_name="Link Imagem 2",
        help_text="URL opcional da imagem 2)"
    )
    banner_url3 = models.URLField(
        blank=True,
        verbose_name="Link Imagem 3",
        help_text="URL opcional da imagem 3)"
    )

    panels = [
        MultiFieldPanel(
            [
            FieldPanel("favicon"),
            FieldPanel("logo"),
            ], heading="Imagens da marca"
        ),
        MultiFieldPanel(
            [
            FieldPanel("banner_image1"),
            FieldPanel("banner_image2"),
            FieldPanel("banner_image3"),
            FieldPanel("banner_url1"),
            FieldPanel("banner_url2"),
            FieldPanel("banner_url3"),
            ], "Configurações do carrossel de banners do Rodapé (800x110px)"),
    ]