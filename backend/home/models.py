from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogPage
from content.models import ContentPage

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

    show_alert    = models.BooleanField(default=True)
    alert         = models.CharField(blank=True, max_length=256)

    def blog_first(self):
        """Returns the most recent blog item."""
        return BlogPage.objects.order_by('-date')[0]

    def blog_follow(self):
        """Returns the second and third blog item."""
        blogs = BlogPage.objects.all()
        blogs = blogs.order_by('-date')[1:3]
        return blogs
    
    content_panels = Page.content_panels + [
        InlinePanel("carousel_images", max_num=5, min_num=1, heading="Karusell Bilder"),
        FieldPanel('show_alert', classname="full", heading="Benachrichtigung anzeigen"),
        FieldPanel('alert', classname="full", heading="Benachrichtigung"),
    ]
