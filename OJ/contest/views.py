from django.shortcuts import render, redirect

from user.models import is_loggedin
from OJ.utils import add_user_information
from .models import get_contests_dict, get_contest_dict, get_new_submission_id, add_submission, \
    add_submission_to_contest, get_submissions_dict, get_mysubmissions_dict, get_problem_id , get_submission_dict
from problem.models import get_problem_dict
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


def submit(request, contest_id, alias=None):
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
            post_data['USER_ID'] = request.session['user_id']
            post_data['CONTEST_ID'] = contest_id

            add_submission(post_data)

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
        context['SUBMISSIONS'] = get_mysubmissions_dict(
            contest_id, request.session['user_id'])
        context = add_user_information(request, context)
    return render(request, 'contest/mysubmissions.html', context)


def status(request, contest_id):
    context = {}

    context = get_contest_dict(contest_id)

    context['SUBMISSIONS'] = get_submissions_dict(contest_id)

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'contest/status.html', context)


def submission(request, contest_id, submission_id):
    context = {}
    context = get_submission_dict(submission_id)
    context.update(get_contest_dict(contest_id))

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'contest/submission.html', context)


def problem(request, contest_id, alias):
    problem_id = get_problem_id(contest_id, alias)
    if problem_id is None:
        return redirect('contest', contest_id)

    context = {}
    context = get_problem_dict(problem_id)

    context['PROBLEM_ID'] = alias
    context.update(get_contest_dict(contest_id))

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'contest/problem.html', context)
