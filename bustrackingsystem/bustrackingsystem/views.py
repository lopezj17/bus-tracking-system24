#from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html')

def main_page(request):
    return render(request, 'main_page.html')

def settings_page(request):
    return render(request, 'settings_page.html')

def account_page(request):
    return render(request, 'account_page.html')

def support_page(request):
    return render(request, 'support_page.html')

def discovery_park_page(request):
    return render(request, 'Discovery_Park.html')
