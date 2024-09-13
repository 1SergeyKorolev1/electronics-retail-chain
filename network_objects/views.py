from rest_framework.viewsets import ModelViewSet, generics
from network_objects.models import Product, Supplier
from network_objects.serializers import ProductSerializer, SupplierSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

