from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer
from .serializers import ProductSerializer
from rest_framework import generics
from .serializers import CustomerSerializer
from .models import Billing

from .serializers import BillingSerializer
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomerForm, ProductForm, BillingForm
from .models import Customer

from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from .models import Product
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm


class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BillingListCreate(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer


class BillingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer


def customers_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm()

    customers = Customer.objects.all()
    return render(request, 'customers.html', {'form': form, 'customers': customers})


def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'update_customer.html', {'form': form, 'customer': customer})


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')


def products_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    products = Product.objects.all()
    return render(request, 'products.html', {'form': form, 'products': products})


def billing_view(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing')
    else:
        customers = Customer.objects.all()
        products = Product.objects.all()

        selected_customer = customers.first()
        return render(request, 'billing.html', {'customers': customers, 'products': products, 'customer': selected_customer})


def create_billing(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            billing = form.save()
            billing_details = {
                'customer': billing.customer,
                'product': billing.product,
                'quantity': billing.quantity
            }
            return render(request, 'billing.html', {'customers': customers, 'products': products, 'billing_details': billing_details})
    else:
        form = BillingForm()
    return render(request, 'billing.html', {'form': form, 'customers': customers, 'products': products})


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'confirm_delete_product.html', {'product': product})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))


def generate_slip(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')  # Retrieve customer_id from the form data
        if customer_id:
            customer = get_object_or_404(Customer, id=customer_id)
            product_id = request.POST.get('product_id')
            quantity = request.POST.get('quantity')
            if product_id and quantity:
                product = get_object_or_404(Product, id=product_id)
                return render(request, 'slip_template.html', {'customer': customer, 'product': product, 'quantity': quantity})
            else:
                return HttpResponse('Product ID or quantity is missing.')
        else:
            return HttpResponse('Customer ID is missing.')
    else:
        return HttpResponse('Invalid request method.')



@login_required
def customer_management(request):
    return render(request, 'customers.html')


@login_required
def product_management(request):
    return render(request, 'products.html')


@login_required
def billing(request):
    # Your view logic here
    return render(request, 'billing.html')









