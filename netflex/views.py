from django.shortcuts import render
from .request import get_currencies

def home(request):
   
    ctx={
      
    }
    return render(request,"netflex/home.html",ctx)

