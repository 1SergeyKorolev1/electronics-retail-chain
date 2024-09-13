from django.contrib import admin
from django.urls import reverse
from network_objects.models import Product, Supplier

@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")

@admin.register(Supplier)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "purveyor_link")

    def purveyor_link(self, obj):
        if obj.purveyor:
            return reverse('admin:network_objects_supplier_change', args=(f'{obj.purveyor.pk}'))
        return obj.purveyor


