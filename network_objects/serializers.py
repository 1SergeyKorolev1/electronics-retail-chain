from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from network_objects.models import Product, Supplier


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"