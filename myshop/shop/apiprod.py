from .models import Product
from rest_framework import viewsets, permissions
from shop.api.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]
    serializer_class = ProductSerializer
