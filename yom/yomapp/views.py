from django.shortcuts import render

# Create your views here.
def yom_html(req):
    return render(req, "yom.html")


def home_html(req):
    return render(req, "home.html")


def pages_html(req):
    if req.method == "POST":
        rollno = req.POST.get("rollno")
        name = req.POST.get("name")
        hindi = req.POST.get("hindi")
        gujarati = req.POST.get("gujarati")
        ss = req.POST.get("ss")
        total = req.POST.get("total")
        minmarks = req.POST.get("minmarks")
        maxmarks = req.POST.get("maxmarks")
        percentage = req.POST.get("percentage")
        grade = req.POST.get("grade")
        context = {
            "Roll No": rollno,
            "Name": name,
            "Hindi": hindi,
            "Gujarati": gujarati,
            "SS": ss,
            "Total": total,
            "min marks": minmarks,
            "max marks": maxmarks,
            "Percentage": percentage,
            "Grade": grade
        }
        return render(req, "pages.html",context)

    return render(req, "pages.html")