from django import forms
from .models import Customer, Product, Billing


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['customer', 'product', 'quantity']


