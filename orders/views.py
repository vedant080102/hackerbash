from django.shortcuts import render
import accounts.views

# Import database module.
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference('https://bookstore-25547-default-rtdb.firebaseio.com')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())

# Create your views here.
