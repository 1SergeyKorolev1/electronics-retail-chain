from rest_framework.viewsets import ModelViewSet
from network_objects.models import Product, Supplier, Contacts
from network_objects.serializers import ProductSerializer, SupplierSerializer, ContactsSerializer
from network_objects.permissions import NotUpdate

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactsViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def perform_create(self, serializer):
        supplier = serializer.save()
        if supplier.purveyor:
            purveyor = supplier.purveyor
            supplier.supplier_level = purveyor.supplier_level + 1
            supplier.save()
            print(supplier)

    def get_permissions(self):
        if self.action in ["partial_update", "update"]:
            if 'debt' in list(self.request.data):
                self.permission_classes = (NotUpdate, )
        return super().get_permissions()

