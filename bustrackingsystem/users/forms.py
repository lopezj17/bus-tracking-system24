from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.fields import EmailField  
from django.contrib.auth.models import User
from django import forms

class user_signup_form(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(label='User ID', min_length=5, max_length=150) 
    #email = forms.EmailField(label="Email")
    #user_id = forms.IntegerField(max_value=99999999)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields[]
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password Confirmation'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

class user_auth_form(AuthenticationForm):
    username = forms.CharField(label='User ID')
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ('username', 'password')