from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_home(request):
    return render(request, 'Solo_Project/index.html')
    #return HttpResponse('This is the home error')

def login(request):
    return render(request, 'Solo_Project/login.html')

def sign_up(request):
    return render(request, 'Solo_Project/signUp.html')