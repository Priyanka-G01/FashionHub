from wsgiref.util import request_uri
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Customer
from django.contrib.auth.decorators import login_required
from apps.product.models import Product
from django.utils.text import slugify
from apps.product.models import Category

# Create your views here.



def become_customer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)

            customer = Customer.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')

    else:
        form = UserCreationForm()

    return render(request,'customer/become_customer.html',{'form': form})

#@login_required
def customer_det(request):
    customer = request.user.customer
    orders = customer.order.all()
    '''
    for order in orders:
        #order.designer_amount = 0
        #order.designer_paid_amount = 0
        #order.fully_paid = True

        for item in order.items.all():
            if item.order.customer == request.user.customer:
                #if item.designer_paid:
                    #order.designer_paid_amount += item.get_total_price()
                #else:
                    #order.designers.designer_amount += item.get_total_price()
                    #order.fully_paid = False
    '''
    return render(request,'customer/customer_det.html',{'customer':customer, 'orders': orders})

#@login_required
def edit_customer(request):
    customer = request.user.customer

    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')

        if name:
            customer.created_by.email = email
            customer.created_by.save()

            customer.name = name
            customer.save()

            return redirect('customer_det')

    return render(request, 'customer/edit_customer.html',{'customer':customer})

