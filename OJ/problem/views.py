from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from user.models import is_loggedin
from .models import get_problems, add_problem, get_owner_user_id, exist_problem, get_problem_dict
from OJ.utils import add_user_information
# Create your views here.


def problems(request):
    if is_loggedin(request):

        if request.method == 'POST':
            add_problem(request.session['user_id'])

        context = {}

        context['problems'] = get_problems(request.session['user_id'])

        context = add_user_information(request, context)
        return render(request, 'problem/problems.html', context)
    else:
        return redirect('signin')


def problem_edit(request, problem_id):
    if is_loggedin(request=request):
        if exist_problem(problem_id) and get_owner_user_id(problem_id) == request.session['user_id']:
            context = {}
            context = get_problem_dict(problem_id)

            context = add_user_information(request, context)
            return render(request, 'problem/edit.html', context)
        else:
            return redirect('problems')
    else:
        return redirect('signin')


def problem_view(request, problem_id):
    if is_loggedin(request=request):
        if exist_problem(problem_id) and get_owner_user_id(problem_id) == request.session['user_id']:
            context = {}
            context = get_problem_dict(problem_id)

            context = add_user_information(request, context)
            return render(request, 'problem/view.html', context)
        else:
            return redirect('problems')
    else:
        return redirect('signin')
