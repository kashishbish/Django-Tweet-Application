from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm #inbuilt form in django
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta: #banani hi pdti h syntax h
        model=Tweet   #konsa model use krna h 
        fields=['text','photo'] #konse konse field use krne h (model m jo nam likhein voi likhna h)

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')   #tuple dena h qki built in form ko use krre h hum