from django.shortcuts import render

# Create your views here.
def yom_html(req):
    return render(req, "yom.html")


def home_html(req):
    return render(req, "home.html")

def pages_html(req):
    if req.method == "POST":
        Rollno = req.POST.get("rno")
        Name = req.POST.get("name")
        Hindi = req.POST.get("hindi")
        Gujarati = req.POST.get("gujarati")
        SS = req.POST.get("ss")
        Total = req.POST.get("total")
        Min_marks = req.POST.get("min_marks")
        Max_marks = req.POST.get("max_marks")
        # Percentage = req.POST.get("percentage")
        Grade = req.POST.get("grade")
         
        if Total:
            try:
                percentage = round(int(Total) / 300 * 100,2)
            except ZeroDivisionError:
                percentage = 0

        print("rno:",Rollno,"name:",Name,"hindi:",Hindi,"gujarati:",Gujarati,"ss:",SS,"total:",Total,"min_marks:",Min_marks,"max_marks:",Max_marks,"percentage:",percentage,"grade:",Grade)
    
    return render(req, "pages.html")