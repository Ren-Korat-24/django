from django.shortcuts import render

# Create your views here.
def html(req):
    return render(req,'index.html') 