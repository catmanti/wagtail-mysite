from django.db import models


class Subscriber(models.Model):
    """Subscribers to our Site"""

    email = models.EmailField(blank=False, null=False,
                              max_length=100, help_text='Email Address')
    full_name = models.CharField(
        blank=False, null=False, max_length=100, help_text='Full Name')

    def __str__(self):
        return self.full_name
