from django.urls import path
from rest_framework.routers import DefaultRouter

from network_objects.apps import NetworkObjectsConfig
from network_objects.views import ProductViewSet, SupplierViewSet

app_name = NetworkObjectsConfig.name

router = DefaultRouter()
router.register(r"product", ProductViewSet, basename="product")
router.register(r"supplier", SupplierViewSet, basename="supplier")

urlpatterns = [
] + router.urls
