from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class LeitbildPage(Page):

    class Meta:
        verbose_name = "Leitbild"

    teamwork   = RichTextField(blank=True)
    community  = RichTextField(blank=True)
    trust      = RichTextField(blank=True)
    learning   = RichTextField(blank=True)
    schoollife = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('teamwork',   heading="Zusammenarbeit"),
        FieldPanel('community',  heading="Gemeinschaft"),
        FieldPanel('trust',      heading="Vertrauen"),
        FieldPanel('learning',   heading="Lernen"),
        FieldPanel('schoollife', heading="Schulleben")
    ]
