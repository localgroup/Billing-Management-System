
from django.urls import path
from .views import CreateUserView, ProductListCreate, generate_slip, register_user
from . import views
from django.contrib.auth import views as auth_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('customers/', views.customers_view, name='customers'),
    path('products/', views.products_view, name='products'),
    path('billing/', views.billing_view, name='billing'),
    path('customers/', views.CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroy.as_view(), name='customer-detail'),
    path('billing/', views.BillingListCreate.as_view(), name='billing-list-create'),
    path('billing/<int:pk>/', views.BillingRetrieveUpdateDestroy.as_view(), name='billing-detail'),
    path('generate-slip/', generate_slip, name='generate_slip'),
    path('generate-slip/<int:customer_id>/', views.generate_slip, name='generate_slip'),
    path('customers/', views.customer_management, name='customer_management'),
    path('products/', views.product_management, name='product_management'),
    path('billing/', views.billing, name='billing'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('customers/<int:customer_id>/update/', views.update_customer, name='update_customer'),
    path('customers/<int:customer_id>/delete/', views.delete_customer, name='delete_customer'),
    path('registration/', register_user, name='register'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


