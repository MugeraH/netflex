from django.shortcuts import render

def home(request):
    ctx={}
    return render(request,"netflex/home.html",ctx)
