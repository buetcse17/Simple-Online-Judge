from django.shortcuts import render , redirect

from user.models import is_loggedin 
from OJ.utils import add_user_information

# Create your views here.

def messages( request ):
    if is_loggedin(request = request):
        context = {}
        
        context = add_user_information(request= request , context= context)
        return render(request , 'messages.html' ,context= context )
    else:
        return redirect('signin')