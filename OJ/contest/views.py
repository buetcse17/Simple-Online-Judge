from django.shortcuts import render, redirect

from user.models import is_loggedin
from OJ.utils import add_user_information
from .models import get_contests_dict, get_contest_dict , get_new_submission_id ,add_submission , add_submission_to_contest
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


def submit(request, contest_id , alias = None):
    if is_loggedin(request):
        if request.method == 'POST':
            
            post_data = request.POST.copy()
            del post_data['csrfmiddlewaretoken']

            if 'RAW_CODE_FILE' in request.FILES:

                data = request.FILES['RAW_CODE_FILE']
                post_data['RAW_CODE'] = data.read().decode('utf-8')
            
            if 'RAW_CODE_FILE' in post_data:
                del post_data['RAW_CODE_FILE']

            submission_id = get_new_submission_id()

            post_data['SUBMISSION_ID'] = submission_id
            
            add_submission(post_data)
            add_submission_to_contest(contest_id , request.session['user_id'] , submission_id)

            return redirect('mysubmissions', contest_id)

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
