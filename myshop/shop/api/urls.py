from rest_framework import routers
from shop.apiprod import ProductViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('products', ProductViewSet, 'product_api' )

urlpatterns = router.urls
