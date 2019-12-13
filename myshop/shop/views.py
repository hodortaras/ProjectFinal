from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import View
from rest_framework import generics
from shop.api.serializers import ProductSerializer


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'shop/product/list.html',context={'category': category,
                                                            'categories': categories,
                                                            'products': products,
                                                            'cart_product_form': cart_product_form})


class ProductDetail(View):
    def get(self,request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        cart_product_form = CartAddProductForm()
        return render(request, 'shop/product/detail.html', context={'product': product,
                                                            'cart_product_form': cart_product_form})


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(id=id)
    serializer_class = ProductSerializer
