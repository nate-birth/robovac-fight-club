from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Support
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='eg. youremail@gmail.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')


class TechSupportForm(forms.ModelForm):
    message=forms.CharField(min_length=2,max_length=255,required=True,widget = forms.Textarea(attrs={'rows': 10, 'cols': 50,'placeholder':'Message here'}))

    class Meta:
        model = Support
        fields = ['message']
        