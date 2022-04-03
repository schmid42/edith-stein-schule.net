from enum import IntEnum

from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable, Collection
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogPage

class CarouselImages(Orderable):
    """Images for the home page carousel"""
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    panels = [
        ImageChooserPanel("carousel_image", classname="full", heading="Karussell Bild")
    ]


class HomePage(Page):

    COLLECTION_CHOICES = ((str(c.id), c.name) for c in Collection.objects.all())


    class Meta:
        verbose_name = "Startseite"

    info     = RichTextField(blank=True)
    video_id = models.CharField(blank=True, max_length=20)

    collection = models.CharField(
        max_length=255,
        choices=COLLECTION_CHOICES,
        blank=True
    )

    def blog_last(self):
        """Returns the first and second blog item."""
        blogs = BlogPage.objects.all()
        blogs = blogs.order_by('-date')[0:2]
        return blogs
    
    def gallery(self):
        items = Image.objects.filter(collection__id=int(self.collection))
        return items
    
    content_panels = Page.content_panels + [
        FieldPanel('info', heading="Aktuelle Infos"), 
        InlinePanel("carousel_images", max_num=5, min_num=1, heading="Karusell Bilder"),
        FieldPanel('video_id', classname="full", heading="Youtube Video ID"),
        FieldPanel('collection', classname="full", heading="Collection"),
    ]

