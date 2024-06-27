from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_page, name='login'),# Login page
    path('signup/', views.sign_up_page, name='signup') # Sign up page
]