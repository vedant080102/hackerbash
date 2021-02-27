from django.shortcuts import render,redirect
from orders.views import bookItems

# Create your views here.

def home(request):
    return render(request,'home.html')

def home1(request):
    return redirect('/home')

def book(request):
    bk=bookItems()
    return render(request,'books.html',{"bk":bk})