from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from network_objects.models import Product, Supplier, Contacts

class IsCityCountryFilter(admin.SimpleListFilter):
    title = 'CityCountry'
    parameter_name = 'city_country'

    def lookups(self, request, model_admin):
        return (
            ('city', 'City'),
            ('country', 'Country'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'city':
            return queryset.order_by('contacts__city')
        if self.value() == 'country':
            return queryset.order_by('contacts__country')
        return queryset

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "country", "city")

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "purveyor_link", "debt", "supplier_level", "city", "country")
    actions = ["clean_debt"]
    list_filter = [IsCityCountryFilter]

    def city(self, obj):
        if obj.contacts:
            return obj.contacts.city
        return obj.contacts

    def country(self, obj):
        if obj.contacts:
            return obj.contacts.country
        return obj.contacts

    def purveyor_link(self, obj):
        if obj.purveyor:
            return format_html('<a href="{0}">{1} {2}</a>'.format(
                reverse(
                    'admin:network_objects_supplier_change',
                    args=(f'{obj.purveyor.pk}')
                ), obj.purveyor, obj.purveyor.pk))
        return obj.purveyor

    def clean_debt(self, request, queryset):
        for supplier in queryset:
            supplier.debt = 0
            supplier.save()
        self.message_user(request, f"Задолженность очищена.")

    clean_debt.short_description = "Очистить задолженность"
    purveyor_link.short_description = "ссылка на поставщика"


