"""StreamFeilds Live in here"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and Text and nothing else"""

    title = blocks.CharBlock(required=True, help_text='Add your Title')
    text = blocks.TextBlock(required=True, help_text="Add additional Text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image, text and buttons"""

    title = blocks.CharBlock(required=True, help_text='Add your Title')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"


class RichTextBlock(blocks.RichTextBlock):
    """RichText with all the features"""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full Richtext"


class SimpleRichTextBlock(blocks.RichTextBlock):
    """RichText with selected features"""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CTABlock(blocks.StructBlock):
    """A Simple call to action section"""
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold', 'italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(
        required=True, default='Learn More', max_length=15)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"
