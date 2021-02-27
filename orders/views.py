from django.shortcuts import render
import accounts.views
from firebase_admin import firestore
# Create your views here.

db=firestore.client()

def bookItems():
    docs = db.collection(u'books').stream()
    books=[]
    for doc in docs:
        books.append(doc.to_dict())
    return books