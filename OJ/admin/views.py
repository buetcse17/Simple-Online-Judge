from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from user.models import is_loggedin, logout
from OJ.utils import add_user_information
from contest.models import get_contests_dict
from admin.models import is_admin, add_contest_db
# Create your views here.


def contests(request):
    if is_loggedin(request) and is_admin(request.session['handle']):
        context = {}
        context['CONTESTS'] = get_contests_dict(request.session.get('user_id'))
        context = add_user_information(request, context)
        return render(request, 'admin/contests.html', context)
    else:
        logout(request)
        return redirect('signin')


def add_contest(request):
    if is_loggedin(request) and is_admin(request.session['handle']):
        add_contest_db()
        return redirect('admin_contests')
    else:
        logout(request)
        return redirect('signin')
