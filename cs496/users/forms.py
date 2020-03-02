from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Extension of the basic user creation form to include extra fields
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')