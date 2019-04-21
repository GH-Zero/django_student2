from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req,"index.html")
def scenery(req):
    return render(req,"scenery.html")
def character(req):
    return render(req,"character.html")
def animmals(req):
    return render(req,"animals.html")
