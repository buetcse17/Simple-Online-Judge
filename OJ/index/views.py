from django.shortcuts import render, redirect
from user.models import is_loggedin
from OJ.utils import add_user_information

# Create your views here.


def index(request):
    context = {}
    if is_loggedin(request=request):
        context = add_user_information(request=request, context=context)
    return render(request, 'index.html', context=context)


def friends(request):
    if is_loggedin(request):
        context = {}

        context = add_user_information(request=request, context=context)
        return render(request, 'friends.html', context)
    else:
        return redirect('signin')
