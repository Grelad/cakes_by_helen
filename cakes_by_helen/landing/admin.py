from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext as _
from landing.models import ImageGallery, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "comment", "type", "date")
    search_fields = ("name__startswith", "phone__startswith")
    readonly_fields = ("date",)


class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'thumbnail',)
    ordering = ("-id",)
    readonly_fields = ("thumbnail",)

    def thumbnail(self, obj):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % obj.image.url)

    thumbnail.short_description = _('Image')


admin.site.register(ImageGallery, ImageGalleryAdmin)
admin.site.register(Order, OrderAdmin)
