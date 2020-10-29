from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from user.models import authenticate , login , handle_exists , email_exists , add_user  , get_hash

def signup(request):
    if request.method == 'POST':
        handle = request.POST['handle'].lower()
        email = request.POST['email'].lower()
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        print (handle , email , name , password1 , password2 )

        if handle_exists(handle = handle):
            messages.info(request , 'Handle already in use')
            return redirect('signup')
        elif email_exists(email = email):
            messages.info(request , 'Email already in use')
            return redirect('signup')
        elif password1 != password2 :
            messages.info(request , 'Password dont match')
            return redirect('signup')
        else :
            if add_user(handle = handle , email = email , name = name , password_hash = get_hash(password1) ):
                return redirect("/")
            else:
                messages.info(request , 'Server Error')
                return redirect('signup')
    else :
        return render(request , 'signup.html' )