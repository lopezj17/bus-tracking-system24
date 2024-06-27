#from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    #return HttpResponse('Welcome to the Bus Tracking System!')+
    return render(request, 'home_page.html')

def main_page(request):
    #return HttpResponse('Main map and bus page.')
    return render(request, 'main_page.html')

'''
def login_page(request):
    #return HttpResponse('Welcome to the Bus Tracking System!')+
    return render(request, 'login_page.html')

def sign_up_page(request):
    #return HttpResponse('User registration page.')
    return render(request, 'signup_page.html')    
'''
