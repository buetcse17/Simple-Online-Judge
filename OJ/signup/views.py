from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        handle = request.POST['handle']
        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        print (handle , email , name , password1 , password2 )

        return redirect("/")

    else :
        return render(request , 'signup.html' )