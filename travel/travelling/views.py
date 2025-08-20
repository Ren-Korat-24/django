from django.shortcuts import render,redirect,get_object_or_404
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

def showdata(req):
    data = Homehtml.objects.all().values()
    return render(req,"show.html",{"data":data})

def deletedata(req,id):
    Homehtml.objects.filter(id=id).delete()
    return redirect("/show")

def editdata(req,id):
    try:
        data1=Homehtml.objects.get(id=id)
    except:
        print("record not found")
    if "submit" in req.POST:
        data1.name=req.POST['name']
        data1.email=req.POST['email']     
        data1.save()
        print("Successfully Upadated.....")
        return redirect("/show")
    return render(req,"home.html",{"data1":data1})