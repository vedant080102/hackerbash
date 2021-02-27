from django.urls import path
from . import views

urlpatterns=[
    path('login',views.login,name="login"),
    path('cart',views.cart,name="cart"),
    path('signup',views.signup,name="signup")
]