from django.shortcuts import render, redirect

from user.models import is_loggedin
from OJ.utils import add_user_information
from .models import get_contests_dict, get_contest_dict
# Create your views here.


def contests(request):
    context = {}

    context['CONTESTS'] = get_contests_dict()
    print(context)

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'contest/contests.html', context)


def contest(request, contest_id):
    context = {}

    context = get_contest_dict(contest_id)

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'contest/dashboard.html', context)


def submit(request, contest_id):
    if is_loggedin(request):
        if request.method == 'POST':
            problem_id = request.POST.get('PROBLEM_ID')
            
        else:
            context = {}
            context = get_contest_dict(contest_id)

            context = add_user_information(request, context)
            return render(request, 'contest/submit.html', context)
    else:
        return redirect('signin')


def mysubmissions(request, contest_id):
    context = {}

    context = get_contest_dict(contest_id)

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'contest/mysubmissions.html', context)
