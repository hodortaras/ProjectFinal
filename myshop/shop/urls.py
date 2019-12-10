from django.urls import path
from .views import product_list, ProductDetail
from django.conf.urls import url

app_name = 'shop'

urlpatterns = urlpatterns = [
    path('', product_list, name='product_list'),
    path('<category_slug>/', product_list, name='product_list_by_category'),
    path('<id>/<slug>/', ProductDetail.as_view(), name='product_detail'),
]
