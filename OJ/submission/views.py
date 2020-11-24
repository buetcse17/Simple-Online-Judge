from django.shortcuts import render , redirect

from user.models import is_loggedin , handle_exists
from OJ.utils import add_user_information
from .models import get_submissions_all_dict , get_submissions_user_dict
# Create your views here.

def submissions(request):
    context = {}

    context['SUBMISSIONS'] = get_submissions_all_dict()

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'submission/all.html', context)

def submissions_user(request, handle):
    if not handle_exists(handle):
        return redirect('submissions')

    context = {}
    context['SUBMISSIONS'] = get_submissions_user_dict(handle)

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'submission/user.html', context)