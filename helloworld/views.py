from django.shortcuts import render
from helloworld import views
from django.shortcuts import HttpResponse

def home(res):
    return render(res,"index.html")