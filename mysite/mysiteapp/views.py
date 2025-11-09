# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import Register
from django.db.models import Q
from django.core.paginator import Paginator


def form_page(req):
    if req.method == "POST":
        name = req.POST.get("name")
        email = req.POST.get("email")
        contact = req.POST.get("contact")
        password = req.POST.get("password")
        cpassword = req.POST.get("cpassword")

        if password != cpassword:
            return render(req, "form.html", {"msg": "Passwords do not match"})

        # Check if Register already exists
        if Register.objects.filter(email=email).exists():
            return render(req, "form.html", {"msg": "Email already registered!"})

        # Save Register
        Register.objects.create(
            name=name, email=email, contact=contact, password=password
        )
        # print("data inserted..")
        return redirect("login")

    return render(req, "form.html")


def index_page(req):
    if req.method == "POST":
        email = req.POST.get("email")
        password = req.POST.get("password")

        # Check if Register exists
        if not Register.objects.filter(email=email).exists():
            return render(req, "index.html", {"msg": "First create an account!"})

        # Check password
        if Register.objects.filter(email=email, password=password).exists():
            return render(req, "navbar.html")

        return render(req, "index.html", {"msg": "Wrong password!"})

    return render(req, "index.html")


def logout_page(req):
    if req.method == "POST":
        return redirect("login")


def dashboard_page(req):
    return render(req, "dashboard.html")


def users_page(req):
    if "submit" in req.POST:
        search_query = req.GET.get("search")
        data = Register.objects.filter(new_collection=search_query).values()
        return render(req, "users.html", {"data": data})

    data = Register.objects.all()
    paginator = Paginator(data, 10)  # Show 25 contacts per page.

    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(req, "users.html", {"page_obj": page_obj})  # fetch all users from DB


def delete_data(req, id):
    Register.objects.filter(id=id).delete()
    return redirect("/users")


def edit_data(req, id):
    user = Register.objects.get(id=id)

    if "submit" in req.POST:
        user.name = req.POST.get("name")
        user.email = req.POST.get("email")
        user.contact = req.POST.get("contact")
        user.password = req.POST.get("password")
        user.save()
        print("User  Data  Updated..")
        return redirect("users")

    return render(req, "form.html", {"user": user})

def search_data(req):
    query = req.GET.get("query")  # matches your form input name
    if query:
        data = Register.objects.filter(
            Q(name__icontains=query) | Q(contact__icontains=query) | Q(email__icontains=query) | Q(password__icontains=query)).distinct()
    else:
        data = Register.objects.all()  

    paginator = Paginator(data, 10)
    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(req, "users.html", {"data": data, "page_obj": page_obj, "query": query})

def navigation_bar(req):
    return render(req, "nav.html")


def footer_bar(req):
    return render(req, "footer.html")


def blogs_page(req):
    if "submit" in req.POST:
        search_query = req.GET.get("search")
        data = Register.objects.filter(new_collection=search_query).values()
        return render(req, "blogs.html", {"data": data})

    data = Register.objects.all()
    paginator = Paginator(data, 1)  # Show 25 contacts per page.

    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(req, "blogs.html", {"page_obj": page_obj})


def home_page(req):
    if req.method == "POST":
        email = req.POST.get("email")
        password = req.POST.get("password")

        # Check if Register exists
        if not Register.objects.filter(email=email).exists():
            return render(req, "index.html", {"msg": "First create an account!"})

        # Check password
        if Register.objects.filter(email=email, password=password).exists():
            return render(req, "home.html")

        # Wrong password
        return render(req, "index.html", {"msg": "Wrong password!"})

    return render(req, "home.html")
