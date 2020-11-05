from django.shortcuts import render, redirect
from django.http import Http404

from user.models import is_loggedin
from OJ.utils import add_user_information
from user.models import handle_exists
# Create your views here.


def messages(request):
    if is_loggedin(request=request):
        context = {}

        context = add_user_information(request=request, context=context)
        return render(request, 'messages.html', context=context)
    else:
        return redirect('signin')


def conversation(request, handle):
    if is_loggedin(request=request):
        if handle_exists(handle=handle):
            context = {}
            context = add_user_information(request=request, context=context)
            return render(request, 'messages.html', context=context)
        else:
            raise Http404('No such user')
    else:
        return redirect('signin')
