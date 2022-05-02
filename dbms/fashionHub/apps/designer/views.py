import imp
from wsgiref.util import request_uri
from colorama import Cursor
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Designer
from django.contrib.auth.decorators import login_required
from apps.product.models import Product
from .forms import Productform
from django.utils.text import slugify
from apps.product.models import Category
from apps.core.models import User
# Create your views here.



def become_designer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)

            designer = Designer.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')

    else:
        form = UserCreationForm()

    return render(request,'designer/become_designer.html',{'form': form})

@login_required
def designer_admin(request):
    designer = request.user.designer
    products = designer.products.all()
    orders = designer.orders.all()

    for order in orders:
        order.designer_amount = 0
        order.designer_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.designer == request.user.designer:
                if item.designer_paid:
                    order.designer_paid_amount += item.get_total_price()
                else:
                    order.designer_amount += item.get_total_price()
                    order.fully_paid = False


    return render(request,'designer/designer_admin.html',{'designer':designer,'products':products, 'orders': orders})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = Productform(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.designer = request.user.designer
            product.slug = slugify(product.title)
            product.save()

            return redirect('designer_admin')
    
    else:
        form = Productform()

    return render(request, 'designer/add_product.html',{'form':form})

@login_required
def edit_designer(request):
    designer = request.user.designer

    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')

        if name:
            designer.created_by.email = email
            designer.created_by.save()

            designer.name = name
            designer.save()

            return redirect('designer_admin')

    return render(request, 'designer/edit_designer.html',{'designer':designer})

from django.db import connection
cursor = connection.cursor()
def designers(request):
    #designers = Designer.objects.all()
  
    cursor.execute('call showAllDesigners')
    d = cursor.fetchall()
    designers = list(d)
    return render(request, 'designer/designers.html',{'designers':designers})
    

def designer(request, designer_id):
    designer = get_object_or_404(Designer, pk=designer_id)
    

    return render(request, 'designer/designer.html',{'designer':designer})
