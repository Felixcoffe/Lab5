from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def carreras(request):
    titulo = "<h><>"
    return HttpResponse("carreras")

def docentes(request):
    return HttpResponse("docentes")