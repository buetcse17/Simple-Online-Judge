from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from user.models import is_loggedin, logout , handle_exists , get_user_id
from OJ.utils import add_user_information
from contest.models import get_contests_dict, get_contest_dict
from admin.models import is_admin, add_contest_db, remove_contest_db , update_contest_db , add_manager , remove_manager_db

from datetime import datetime
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


def remove_contest(request, contest_id):
    if is_loggedin(request) and is_admin(request.session['handle']):
        remove_contest_db(contest_id)
        return redirect('admin_contests')
    else:
        logout(request)
        return redirect('signin')


def contest(request, contest_id):
    if is_loggedin(request) and is_admin(request.session['handle']):
        if request.method == 'POST':

            post_data = (request.POST).copy()
            del post_data['csrfmiddlewaretoken']

            manager_handle = post_data['MANAGER_HANDLE']
            del post_data['MANAGER_HANDLE']

            if manager_handle != '' and handle_exists(manager_handle):
                manager_user_id = get_user_id(manager_handle)
                add_manager(contest_id , manager_user_id)
            

            # print((post_data['START_TIME']))
            start_time_str = post_data['START_TIME']
            if start_time_str == '':
                start_time = None
            else:
                start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
            post_data['START_TIME'] = start_time

            #print(post_data)
            
            if post_data['DURATION'] == '':
                post_data['DURATION'] = None
            else:
                post_data['DURATION'] = int(post_data['DURATION'])
            
            post_data['CONTEST_ID'] = contest_id
            #print(type(post_data['DURATION']))


            update_contest_db(post_data)

            return redirect('admin_contest' , contest_id)

        context = get_contest_dict(contest_id)
        context = add_user_information(request, context)
        return render(request, 'admin/contest.html', context)
    else:
        logout(request)
        return redirect('signin')


def remove_manager(request , contest_id , manager_id):
    if is_loggedin(request) and is_admin(request.session['handle']):
        remove_manager_db(contest_id , manager_id)
        return redirect('admin_contest' , contest_id)
    else:
        logout(request)
        return redirect('signin')