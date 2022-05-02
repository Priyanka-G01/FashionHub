import imp
from django.shortcuts import render, get_object_or_404,redirect
import random 
from .models import Category,Product
from .forms import AddToCartForm
from django.contrib import messages
from apps.cart.cart import Cart
# Create your views here.

def search(request):
    name = request.POST['query']
    products = Product.objects.filter(title__icontains=name)
    
    return render(request, 'product/search.html', {'products': products,'query':name})

def product(request, category_slug, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    form_class = AddToCartForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
       
        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request,"Product added to the cart successfully")

            return redirect('product',category_slug=category_slug, product_slug=product_slug)
        else:
            form = AddToCartForm()
    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    return render(request,'product/product.html',{'form':form,'product':product,'similar_products':similar_products})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category':category})

