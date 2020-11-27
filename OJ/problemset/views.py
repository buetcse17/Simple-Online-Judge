from django.shortcuts import render, redirect


from .models import get_all_problem_summury_dict
from OJ.utils import add_user_information
from user.models import is_loggedin
from problem.models import get_problem_dict, exist_problem
from submission.models import get_new_submission_id, add_submission, get_submissions_user_dict, get_submissions_all_dict, get_submission_dict

# Create your views here.


def problemset(request):
    context = {}
    context['PROBLEMS'] = get_all_problem_summury_dict()

    return render(request, 'problemset/dashboard.html', context)


def submit(request, alias=None):
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
            post_data['CONTEST_ID'] = None

            add_submission(post_data)

            return redirect('problemset_mysubmissions')

        else:
            context = {}
            context['PROBLEMS'] = get_all_problem_summury_dict()
            context = add_user_information(request, context)
            return render(request, 'problemset/submit.html', context)
    else:
        return redirect('signin')


def problem(request, alias):
    problem_id = int(alias)
    if problem_id is None or not exist_problem(problem_id):
        return redirect('problemset')

    context = {}
    context = get_problem_dict(problem_id)

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'problemset/problem.html', context)


def mysubmissions(request):
    context = {}

    if is_loggedin(request):
        context['SUBMISSIONS'] = get_submissions_user_dict(
            request.session['handle'])
        context = add_user_information(request, context)
    return render(request, 'problemset/mysubmissions.html', context)


def status(request):
    context = {}

    context['SUBMISSIONS'] = get_submissions_all_dict()

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'problemset/status.html', context)


def submission(request, submission_id):
    context = {}
    context = get_submission_dict(submission_id)

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'problemset/submission_view.html', context)
