from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

import uuid


class ContentPageSections(Orderable):
    """TODO"""

    page    = ParentalKey("content.ContentPage", related_name="content_sections")
    heading = models.CharField(blank=True, max_length=256)
    body    = RichTextField(blank=True)
    link    = models.CharField(max_length=36, editable=False, default=uuid.uuid4)

    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    panels = [
        FieldPanel('heading', heading="Überschrift"),
        FieldPanel('cover', heading="Bild zu diesem Abschnitt"),
        FieldPanel('body', heading="Inhalt")
    ]




class ContentPage(Page):

    class Meta:
        verbose_name = "statische Seite"

    heading      = models.CharField(blank=True, max_length=256)
    body         = RichTextField(blank=True)
    show_content = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading', heading="Seitenüberschrift"),
                FieldPanel('body', heading="Inhalt"),               
                FieldPanel('show_content', heading="Seiteninhalt anzeigen")
            ]
        ),        
        InlinePanel('content_sections', heading="Abschnitte")
    ]
