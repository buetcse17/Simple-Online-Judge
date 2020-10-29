from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import Http404

from .models import *

# Create your views here.
def profile(request , handle):
    if handle_exists(handle= handle):
        get_user_context(handle=handle)
        context = { 'handle': handle}
        return render(request , 'profile.html' , context=context )
    else :
        raise Http404('No such User')
        