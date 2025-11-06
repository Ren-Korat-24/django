# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import Register
   

def form_page(req):
    if req.method == "POST":
        name = req.POST.get('name')
        email = req.POST.get('email')
        contact = req.POST.get('contact')
        password = req.POST.get('password')
        cpassword = req.POST.get('cpassword')

        if password != cpassword:
            return render(req, 'form.html', {"msg": "Passwords do not match"})

        # Check if Register already exists
        if Register.objects.filter(email=email).exists():
            return render(req, 'form.html', {"msg": "Email already registered!"})

        # Save Register
        Register.objects.create(
            name=name,
            email=email,
            contact=contact,
            password=password
        )
        # print("data inserted..")
        return redirect('login')

    return render(req,'form.html')

def index_page(req):
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        # Check if Register exists
        if not Register.objects.filter(email=email).exists():
            return render(req, 'index.html', {"msg": "First create an account!"})

        # Check password
        if Register.objects.filter(email=email, password=password).exists():
            return render(req, 'navbar.html')
    
        return render(req, 'index.html', {"msg": "Wrong password!"})

    return render(req,'index.html')

def logout_page(req):
    if req.method == "POST":
        return redirect('login')

# def dashbaord_page(req):
#     return render (req, 'dashboard.html')