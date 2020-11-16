from django.shortcuts import render

from user.models import is_loggedin
from OJ.utils import add_user_information
from .models import *
# Create your views here.


def contests(request):
    context = {}

    context['CONTESTS'] = get_contests_dict()
    print(context)

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'contest/contests.html', context)


def contest(request , contest_id):
    pass
