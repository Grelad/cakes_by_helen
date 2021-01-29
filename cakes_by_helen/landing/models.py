from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Order(models.Model):
    name = models.CharField(max_length=75)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    comment = models.TextField(max_length=75)
    TYPE_CHOICE = [
        ("classic_cake", "Classic Cake"),
        ("custom_cake", "Custom Cake"),
        ("pastries", "Pastries"),
        ("gingerbread", "Gingerbread")
    ]
    type = models.CharField(max_length=12, choices=TYPE_CHOICE, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
