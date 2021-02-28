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

def retBook():
    docs1 = db.collection(u'books').stream()
    bks=[]
    for doc in docs1:
        bks.append(doc.to_dict())
    return bks

def retCart():
    docs1 = db.collection(u'books').stream()
    print(type(docs1))
    bks=[]
    for doc in docs1:
        bks.append(doc.to_dict())
    return bks