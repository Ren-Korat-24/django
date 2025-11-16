from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from yomapp.models import Homedata
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
def yom_html(req):
    return render(req, "yom.html")

def home_html(req):
    return render(req, "yom.html")

def pages_html(req):
    if "submit" in req.POST:
        rollno=req.POST['rno']
        name=req.POST['name']
        hindi=req.POST['hindi']
        gujarati=req.POST['gujarati']
        ss=req.POST['ss']
        total=req.POST['total']
        min_marks=req.POST['min_marks']
        max_marks=req.POST['max_marks']
        # percentage=req.POST['percentage']
        grade=req.POST['grade']
         
        if total:
            try:
                percentage = round(int(total) / 300 * 100,2)
            except ZeroDivisionError:
                percentage = 0
        
        data = Homedata(
            rollno=rollno,
            name=name,
            hindi=hindi,
            gujarati=gujarati,
            ss=ss,
            total=total,
            min_marks=min_marks,
            max_marks=max_marks,
            percentage=percentage,
            grade=grade
        )

        data.save()
        print("Data Inserted..")
    return render(req, "pages.html")

def showdata(req):
    if "submit  " in req.POST:
        search_query = req.GET.get("search")
        data = Homedata.objects.filter(new_collection=search_query).values()
        return render(req, "showdata.html",{"data":data})    

    data = Homedata.objects.all().values()
    paginator = Paginator(data, 3)  # Show 10 posts per page.
    
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    return render(req,"showdata.html",{"page_obj":page_obj})

def deletedata(req,id):
    Homedata.objects.filter(id=id).delete()
    return redirect("/show")
    # return render(req,"showdata.html")

def editdata(req,id):
    studentdata =Homedata.objects.get(id=id) 
    if "submit" in req.POST:
        studentdata.rollno=req.POST['rno']
        studentdata.name=req.POST['name']
        studentdata.hindi=req.POST['hindi']
        studentdata.gujarati=req.POST['gujarati']
        studentdata.ss=req.POST['ss']
        studentdata.total=req.POST['total']
        studentdata.min_marks=req.POST['min_marks']
        studentdata.max_marks=req.POST['max_marks']
        studentdata.grade=req.POST['grade']
         
        if studentdata.total:
            try:
                studentdata.percentage = round(int(studentdata.total) / 300 * 100,2)
            except ZeroDivisionError:
                studentdata.percentage = 0

        studentdata.save()
        print("Data Updated..")
        return redirect("/show")
    return render(req,"pages.html",{"Student Data":studentdata})

def searchdata(req):
    query = req.GET.get("query")
    
    if query:
        print("Search Query:", query)
        data = Homedata.objects.filter(name__icontains=query)
        print("Filtered Data:", data)
    else:
        data = Homedata.objects.all()

    paginator = Paginator(data, 3)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(req, "showdata.html", {"page_obj": page_obj, "query": query})

