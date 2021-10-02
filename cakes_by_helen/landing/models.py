from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


TYPE_CHOICE = [
        ("classic_cake", _("Classic Cake")),
        ("custom_cake", _("Custom Cake")),
        ("pastries", _("Pastries")),
        ("gingerbread", _("Gingerbread"))
    ]


class Order(models.Model):
    name = models.CharField(max_length=75)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    comment = models.TextField(max_length=75)
    type = models.CharField(max_length=12, choices=TYPE_CHOICE, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-date",)
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return str(self.id)


class ImageGallery(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1500)
    category = models.CharField(max_length=12, choices=TYPE_CHOICE, blank=True, null=True)
    image = models.ImageField()

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Gallery")
