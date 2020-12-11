from django.shortcuts import render , HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from user.models import authenticate , login  ,get_hash , logout


# Create your views here.

def signin(request):
    if request.method == 'POST':
        handle = request.POST['handle'].lower()
        password = request.POST['password']
        
        if authenticate(handle = handle , password_hash = get_hash(password)):
            login(request , handle)
            #request.session['handle'] = handle
            return redirect('/')
        else :
            messages.info(request , 'Invalid Credentials!!!')
            return redirect('signin')
    else :
        return render(request , 'signin.html')
def signout(request):
    logout(request = request)
    return redirect("/")


