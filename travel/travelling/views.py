from django.shortcuts import render
from travelling.models import Homehtml

# Create your views here.
def html(req):
    return render(req,'index.html') 

def home_html(req):
    if "submit" in req.POST:
        name=req.POST['name']
        email=req.POST['email']
        print(name,email)

        data =Homehtml(
        name=name,
        email=email
        )  
        
        data.save()
        print("Successfully Insertes.....")

    return render(req,'home.html')