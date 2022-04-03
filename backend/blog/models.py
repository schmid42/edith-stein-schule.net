from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class BlogIndexPage(Page):

    class Meta:
        verbose_name = "Beitragsübersicht"

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
        )
    ]

class BlogPage(Page):

    class Meta:
        verbose_name = "Beitrag"

    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date', classname="full", heading="Veröffentlicht am"),
        ImageChooserPanel('cover', classname="full", heading="Bild zu dieser Seite"),
        FieldPanel('body', classname="full", heading="Inhalt"),
    ]


