from django.contrib import admin
from landing.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "comment", "type", "date")
    search_fields = ("name__startswith", "phone__startswith")
    ordering = ("-date",)
    readonly_fields = ("date",)


admin.site.register(Order, OrderAdmin)
