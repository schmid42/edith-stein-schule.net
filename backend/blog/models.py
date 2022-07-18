from django.db import models

from wagtail.core.models import Page, Collection
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index

register_snippet(Collection)

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

    # Verbose name as shown to the user
    class Meta:
        verbose_name = "Beitrag"

    # get all items from associated collection
    def gallery(self):
        return Image.objects.filter(collection__id=self.collection.id)

    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date', classname="full", heading="Veröffentlicht am"),
        ImageChooserPanel('cover', classname="full", heading="Bild zu dieser Seite"),
        FieldPanel('body', classname="full", heading="Inhalt"),
        SnippetChooserPanel('collection', classname="full", heading="Bildergallerie")
    ]
