from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.contrib.settings.models import BaseSetting, register_setting

from streams import blocks


@register_setting
class SocialMediaSettings(BaseSetting):
    """Social Media settings for our custom website. Idially this should be in
    a New App"""
    facebook = models.URLField(blank=True, null=True, help_text="FaceBook Url")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter Url")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Url")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),

        ], heading="Social Media Settings")
    ]


class HomePageCarouselImeges(Orderable):
    """Between 1 and 5 Images of HomePage Carousel"""

    page = ParentalKey("home.HomePage", related_name="carousel_images")

    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    panels = [
        ImageChooserPanel('carousel_image'),
    ]


class HomePage(Page):
    """home page model"""
    template = "home/home_page.html"
    max_count = 1
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_sub_title = RichTextField(
        features=["h2", "h3", "ol", "ul", "bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    banner_cla = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_sub_title"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cla"),
        ], heading="banner_options"),
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=5,
                        min_num=1, label='Image'),
        ], heading="Carousel_Images"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
