from django.urls import path
from .views import cart_detail, cart_add, cart_remove
from django.conf.urls import url

app_name = 'cart'

urlpatterns = [
    # url(r'^$', cart_detail, name='cart_detail'),
    # url(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    # url(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
    path('', cart_detail, name='cart_detail'),
    path('add/<product_id>', cart_add, name='cart_add'),
    path('remove/<product_id>', cart_remove, name='cart_remove'),
]
