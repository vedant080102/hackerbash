from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request,'home.html')

def home1(request):
    return redirect('/home')

def book(request):
    return render(request,'books.html')