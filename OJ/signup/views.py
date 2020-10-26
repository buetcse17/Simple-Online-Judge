from django.shortcuts import render

# Create your views here.
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username','first_name' ,  'email', 'password1', 'password2', )

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    else:
        form = SignUpForm()
    return render(request , 'signup.html' , {'title' : 'Sign Up' , 'form' : form })