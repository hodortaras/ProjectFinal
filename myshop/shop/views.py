from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.urls import reverse



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'shop/product/list.html',{'category': category,
                                                    'categories': categories,
                                                    'products': products,
                                                    'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

# def base(request, category_slug=None):
#     categories = Category.objects.all()
#     products = Product.objects.all()
#     cart_product_form = CartAddProductForm()
#     context = {
#         'categories': categories,
#         'products'  : products,
#         'cart_product_form': cart_product_form
#         }
#
#     return render(request, 'shop/base.html', context )
