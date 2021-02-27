from django.shortcuts import render,redirect
from orders.views import bookItems,retBook

# Create your views here.

def home(request):
    return render(request,'home.html')

def home1(request):
    return redirect('/home')

def book(request):
    bk=bookItems()
    return render(request,'books.html',{"bk":bk})

def iBook(request,name):
    books=retBook()
    for j in books:
        if(j['Bname']==name):
            bkn=name
            bka=j['Author']
            bkg=j['Genre']
            bkp=j['Price']
            bks=j['Summary']
    return render(request,'iBook.html',{"bkn":bkn,"bka":bka,"bkg":bkg,"bkp":bkp,"bks":bks})