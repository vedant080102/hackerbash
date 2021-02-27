from django.urls import path
from . import views

urlpatterns=[
    path('',views.home1,name="default"),
    path('home',views.home,name="home"),
    path('book',views.book,name="book")
            ]