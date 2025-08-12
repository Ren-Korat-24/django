from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cdmi_data(req):
    return render(req, "cdmi.html")

def nav_bar(req):
    return render(req, "navbar.html")

def home(req):
    return HttpResponse("THis is more about the home page.Here we are looking @@@@@@@@@...")

def about(req):
    return render(req, "about.html")

def services(req):
    return render(req, "services.html")

def contact(req):
    return render(req, "contact.html")
