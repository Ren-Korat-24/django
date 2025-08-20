from django.shortcuts import render,redirect,get_object_or_404
from yomapp.models import Homedata

# Create your views here.
def yom_html(req):
    return render(req, "yom.html")

def home_html(req):
    return render(req, "home.html")

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

        # print("rno:",Rollno,"name:",Name,"hindi:",Hindi,"gujarati:",Gujarati,"ss:",SS,"total:",Total,"min_marks:",Min_marks,"max_marks:",Max_marks,"percentage:",Percentage,"grade:",Grade)
        
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
    data = Homedata.objects.all().values()
    return render(req,"showdata.html",{"data":data})

def deletedata(req,id):
    Homedata.objects.filter(id=id).delete()
    return redirect("/show")
    # return render(req,"showdata.html")

# def editdata(req,rollno):
#     data1=Homedata.objects.get(rollno=rollno)
#     data1.save()
#     return render(req,"showdata.html")
#     # return redirect("/show")

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
        # percentage=req.POST['percentage']
        studentdata.grade=req.POST['grade']
         
        if studentdata.total:
            try:
                studentdata.percentage = round(int(studentdata.total) / 300 * 100,2)
            except ZeroDivisionError:
                studentdata.percentage = 0

        # print("rno:",Rollno,"name:",Name,"hindi:",Hindi,"gujarati:",Gujarati,"ss:",SS,"total:",Total,"min_marks:",Min_marks,"max_marks:",Max_marks,"percentage:",Percentage,"grade:",Grade)
        
        # data = Homedata(
        # rollno=rollno,
        # name=name,
        # hindi=hindi,
        # gujarati=gujarati,
        # ss=ss,
        # total=total,
        # min_marks=min_marks,
        # max_marks=max_marks,
        # percentage=percentage,
        # grade=grade
        # )

        studentdata.save()
        print("Data Updated..")
        return redirect("/show")
    return render(req,"pages.html",{"Student Data":studentdata})
