from django.db import models

from wagtail.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey


# Create your models here.

class Photos(Orderable):
    """Images for the home page carousel"""
    page = ParentalKey("photowall.PhotoWallPage", related_name="photos")

    heading = models.CharField(blank=False, max_length=255)
    photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    description = models.CharField(blank=True, max_length=255)

    panels = [
        FieldPanel('heading', classname="full", heading="Überschrift"),
        FieldPanel('photo', classname="full", heading="Foto"),
        FieldPanel('description', classname="full", heading="Beschreibung")
    ]


class PhotoWallPage(Page):

    class Meta:
        verbose_name = "Fotowand"
    
    content_panels = Page.content_panels + [
        InlinePanel("photos", heading="Fotos")
    ]