from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from network_objects.models import Product, Supplier

@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")

@admin.register(Supplier)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "purveyor_link")

    def purveyor_link(self, obj):
        if obj.purveyor:
            return format_html('<a href="{0}">{1}</a>'.format(
                reverse('admin:network_objects_supplier_change', args=(f'{obj.purveyor.pk}')), obj.purveyor))
        return obj.purveyor

    purveyor_link.short_description = "ссылка на поставщика"


