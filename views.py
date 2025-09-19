from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, EVSU!")

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def about(request):
    context = {
        'Name': '',
        'Student_ID': 'Student_ID_Here.'
    }
    return render(request, 'about.html', context)


