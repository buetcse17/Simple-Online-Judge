from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from user.models import is_loggedin, logout
from OJ.utils import add_user_information
from contest.models import get_contests_dict
# Create your views here.


def contests(request):
    if is_loggedin(request) and request.session['handle'] == 'admin':
        context = {}
        context['CONTESTS'] = get_contests_dict(request.session.get('user_id'))
        context = add_user_information(request, context)
        return render(request, 'admin/contests.html', context)
    else:
        logout(request)
        return redirect('signin')
