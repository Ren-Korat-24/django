from django.shortcuts import render
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
        percentage=req.POST['percentage']
        grade=req.POST['grade']
         
        # if Total:
        #     try:
        #         percentage = round(int(Total) / 300 * 100,2)
        #     except ZeroDivisionError:
        #         percentage = 0

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