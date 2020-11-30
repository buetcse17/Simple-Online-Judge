from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from user.models import is_loggedin
from .models import get_problems, add_problem, get_owner_user_id, exist_problem, get_problem_dict, update_problem, \
    get_sample_testcases_dict, add_sample_testcase, remove_sample_testcase , remove_problem
from OJ.utils import add_user_information
# Create your views here.


def problems(request):
    if is_loggedin(request):

        if request.method == 'POST':
            add_problem(request.session['user_id'])
            return redirect('problems')

        context = {}

        context['problems'] = get_problems(request.session['user_id'])

        context = add_user_information(request, context)
        return render(request, 'problem/problems.html', context)
    else:
        return redirect('signin')

def problem_remove(request , problem_id):
    if is_loggedin(request=request):
        if exist_problem(problem_id) and get_owner_user_id(problem_id) == request.session['user_id']:
            remove_problem(problem_id)
            return redirect('problems')
        else:
            return redirect('problems')
    else:
        return redirect('signin')

def problem_edit(request, problem_id):
    if is_loggedin(request=request):
        if exist_problem(problem_id) and get_owner_user_id(problem_id) == request.session['user_id']:
            if request.method == 'POST':

                post_data = (request.POST).copy()

                del post_data['csrfmiddlewaretoken']
                post_data['PROBLEM_ID'] = problem_id

                update_problem(post_data)
                return redirect('problem_edit', problem_id)

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


def add_sample(request, problem_id):
    if is_loggedin(request=request):
        if exist_problem(problem_id) and get_owner_user_id(problem_id) == request.session['user_id']:

            if request.method == 'POST':

                post_data = request.POST.copy()

                del post_data['csrfmiddlewaretoken']

                post_data['PROBLEM_ID'] = problem_id
                post_data['SAMPLE_TESTCASE_ID'] = int(
                    post_data['SAMPLE_TESTCASE_ID'])

                print(post_data)
                print(post_data['INPUT'])

                add_sample_testcase(post_data)
                return redirect('problem_add_sample', problem_id)

            context = {}
            context['SAMPLE_TESTCASES'] = get_sample_testcases_dict(problem_id)

            context = add_user_information(request, context)
            return render(request, 'problem/add_sample.html', context)
        else:
            return redirect('problems')
    else:
        return redirect('signin')


def remove_sample(request, problem_id, sample_testcase_id):
    if is_loggedin(request=request):
        if exist_problem(problem_id) and get_owner_user_id(problem_id) == request.session['user_id']:
            remove_sample_testcase(problem_id, sample_testcase_id)
            return redirect('problem_add_sample', problem_id)
        else:
            return redirect('problems')
    else:
        return redirect('signin')
