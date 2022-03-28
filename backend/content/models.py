from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ContentPageSections(Orderable):
    """TODO"""
    page    = ParentalKey("content.ContentPage", related_name="content_sections")
    heading = models.CharField(blank=True, max_length=256)
    body    = RichTextField(blank=True)

    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    panels = [
        FieldPanel('heading', heading="Überschrift"),
        ImageChooserPanel('cover', heading="Bild zu diesem Abschnitt"),
        FieldPanel('body', heading="Inhalt")
    ]




class ContentPage(Page):


    show_heading    = models.BooleanField(default=True)
    heading         = models.CharField(blank=True, max_length=256)
    show_body    = models.BooleanField(default=True)
    body            = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading', heading="Seitenüberschrift"),
                FieldPanel('show_heading', heading="Seitenüberschrift anzeigen"),
                FieldPanel('body', heading="Inhalt"),               
                FieldPanel('show_body', heading="Seiteninhalt anzeigen")
            ]
        ),        
        InlinePanel('content_sections', heading="Abschnitte")
    ]
