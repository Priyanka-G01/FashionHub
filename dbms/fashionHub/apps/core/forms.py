from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.db import transaction
from apps.customer.models import Customer
from apps.designer.models import Designer

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required= True)
    last_name = forms.CharField(required= True)
    email = forms.EmailField(required = True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(created_by= user)
        customer.email = self.cleaned_data.get('email')
        customer.save()
        return user

class DesignerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required= True)
    last_name = forms.CharField(required= True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_designer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        designer = Designer.objects.create(created_by= user)
        designer.save()
        return user
