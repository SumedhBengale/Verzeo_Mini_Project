import email
from django.shortcuts import render
from django.template.loader import render_to_string


# Create your views here.
def home(request):

    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def courses(request):
    return render(request,'courses.html')