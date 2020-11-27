from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from user.models import is_loggedin

# Create your views here.

def admin(request):
    if is_loggedin(request):
        return render(request, 'admin/layout.html')
    else:
        return 
