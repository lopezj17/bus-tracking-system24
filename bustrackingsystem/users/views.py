from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
#from .forms import user_signup_form

# Create your views here.
def sign_up_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, "signup_page.html", { "form": form})

def login_page(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("main")
    else: 
        form = AuthenticationForm()
    return render(request, "login_page.html", { "form": form })