from django.shortcuts import render, redirect


from user.models import is_loggedin
from .models import get_problems ,add_problem
from OJ.utils import add_user_information
# Create your views here.


def problems(request):
    if is_loggedin(request):

        if request.method == 'POST':
            add_problem(request.session['user_id'])

        context = {}

        context['problems'] = get_problems(request.session['user_id'])

        context = add_user_information(request, context)
        return render(request, 'problems.html', context)
    else:
        return redirect('signin')


def problem_edit(request, problem_id):
    if is_loggedin(request=request):
        pass
    else:
        return redirect('signin')
