from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Subscriber


class SubscriberAdmin(ModelAdmin):
    """Subscribers"""

    model = Subscriber
    menu_label = 'Subscribers'  # ditch this to use verbose_name_plural from model
    menu_icon = 'group'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = False
    list_display = ('email', 'full_name')
    search_fields = ('email', 'full_name')


modeladmin_register(SubscriberAdmin)
