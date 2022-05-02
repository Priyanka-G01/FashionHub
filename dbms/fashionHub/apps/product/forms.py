from socket import fromshare
from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()