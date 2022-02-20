from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class ContentPage(Page):

    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    show_heading    = models.BooleanField(default=True)
    heading         = models.CharField(blank=True, max_length=256)
    show_subheading = models.BooleanField(default=True)
    subheading      = models.CharField(blank=True, max_length=256)
    body            = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('show_heading', classname="full", heading="Seitentitel anzeigen"),
        FieldPanel('heading', classname="full", heading="Seitentitel"),
        FieldPanel('show_subheading', classname="full", heading="Untertitel anzeigen"),
        FieldPanel('subheading', classname="full", heading="Untertitiel"),
        ImageChooserPanel('cover', classname="full", heading="Bild zu dieser Seite"),
        FieldPanel('body', classname="full", heading="Inhalt")
    ]
