from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class user_signup_form(UserCreationForm):
    email = forms.EmailField
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    user_id = forms.IntegerField(max_value=99999999)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_id', 'password1', 'password2')