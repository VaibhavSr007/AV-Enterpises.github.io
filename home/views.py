from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Update
from django.contrib import messages

# Create your views here.
def index(request):
    # context = {
    #     "var1" : " this shows var1",
    #     "var2" : 5
    # }
    return render(request,"index.html")
            # (what req, where, any varialble if want to pass)

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        prep = request.POST.get('prep')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, prep=prep, phone=phone, desc=desc)   
        contact.save() 
        messages.success(request, 'Your data has been updated!')     

    return render(request,"contact.html")

def saveUpdates(request):
    if request.method == "POST":
        user_email = request.POST.get('user_email')
        updates = Update(user_email=user_email)
        updates.save() 

    return render(request,"index.html")


def process(request):
    return render(request,"process.html")
def ssb(request):
    return render(request,"ssb.html")
def exams(request):
    return render(request,"exams.html")

def explore(request):
    return render(request,"explore.html")

def vaibhav(request):
    return render(request,"vaibhav.html")
def akash(request):
    return render(request,"akash.html")
def vikas(request):
    return render(request,"vikas.html")
def shas(request):
    return render(request,"shas.html")
def sartaj(request):
    return render(request,"sartaj.html")
def leroy(request):
    return render(request,"leroy.html")
