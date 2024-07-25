from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import user_signup_form, user_auth_form

# Create your views here.
def sign_up_page(request):
    if request.method == 'POST':
        form = user_signup_form(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('main')
    else:
        form = user_signup_form
    return render(request, "signup_page.html", { "form": form})

def login_page(request): 
    if request.method == "POST": 
        form = user_auth_form(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("main")
    else: 
        form = user_auth_form()
    return render(request, "login_page.html", { "form": form })