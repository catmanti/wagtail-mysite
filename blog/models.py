from django.db.models import CharField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class BlogListingPage(Page):
    intro = CharField(blank=False, null=True, max_length=100, help_text='Overide the defalt Title' )

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
