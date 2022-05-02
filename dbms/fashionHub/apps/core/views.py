from django.shortcuts import render,redirect
from apps.product.models import Product
from django.views.generic import CreateView
from .models import User
from .forms import CustomerSignUpForm, DesignerSignUpForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    return render(request,'core/frontpage.html',{'newest_products':newest_products})

def contact(request):
    return render(request,'core/contact.html')

def register(request):
    return render(request,'core/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'core/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class designer_register(CreateView):
    model = User
    form_class = DesignerSignUpForm
    template_name = 'core/designer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                if user.is_customer:
                    return redirect('/customers/customer_det/')
                else:
                    return redirect('/designers/designer-admin/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'core/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')