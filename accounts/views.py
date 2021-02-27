from django.shortcuts import render,redirect
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials,auth
from firebase_admin import db
from firebase_admin import firestore
from django.http import JsonResponse
from datetime import datetime, timedelta


import time
import pyrebase
CREDENTIALS_FIREBASE_PATH="accounts/bookstore-25547-firebase-adminsdk-qbq2l-036741a7e5.json"
cred = credentials.Certificate("accounts/bookstore-25547-firebase-adminsdk-qbq2l-036741a7e5.json")
try:
    app = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate(CREDENTIALS_FIREBASE_PATH)
    firebase_admin.initialize_app(cred)

Config = {
    "apiKey": "AIzaSyDrGYXbaeY7sGtfLZ4XZCL0f8DfQ5lQC8M",
    "authDomain": "bookstore-25547.firebaseapp.com",
    "databaseURL":"https://bookstore-25547-default-rtdb.firebaseio.com",
    "projectId": "bookstore-25547",
    "storageBucket": "bookstore-25547.appspot.com",
    "serviceAccount": "accounts/bookstore-25547-firebase-adminsdk-qbq2l-036741a7e5.json",
    "messagingSenderId": "873287613221",
    "appId": "1:873287613221:web:7af869611264adc6b678cc",
    "measurementId": "G-SFYW89CVCM"
  }

pirebase = pyrebase.initialize_app(Config)
authe = pirebase.auth()
# Create your views here.


def login(request):
    if request.method =="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            user = authe.sign_in_with_email_and_password(email,password)
            print(user)
        except:
            message="invalid credentials"
            return render(request,"login.html",{"messg":message})
        #print(user['idToken'])
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        us=authe.current_user
        return render(request, "cart.html",{"e":email,"us":us})
    else:
        us=authe.current_user
        return render(request, "login.html",{"us":us})

def cart(request):
    return render(request,'cart.html')


def signup(request):
    if request.method=="POST":
        try:
            name=request.POST.get("name")
            email=request.POST.get("email")
            password=request.POST.get("password")        
            phone=request.POST.get("phone")
            user = auth.create_user(
            email=email,
            email_verified=False,
            phone_number=phone,
            password=password,
            display_name=name,        
            disabled=False)
            user = authe.sign_in_with_email_and_password(email,password)
            return redirect('/cart')
        except:
            return redirect('/accounts/signup')
    else:    
        us=authe.current_user
        return render(request,'signup.html',{"us":us})