from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updatedItem, name="update_item"),
    path('add-product/', views.ProductAddView.as_view(), name="add_product"),
    path('process_order/', views.processOrder, name="process_order"),
    path('login/', auth_views.LoginView.as_view(template_name="store/login.html"), name="login"),
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
