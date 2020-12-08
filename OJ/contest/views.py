from django.shortcuts import render, redirect

from user.models import is_loggedin
from OJ.utils import add_user_information
from .models import (get_contests_dict, get_contest_dict, get_problem_id, add_participant, remove_participant, remove_clarification_db,
                     add_clarification_question,  is_manager, is_participant, update_clarification, add_problem_contest, remove_problem_contest,
                     get_standings_icpc_dict, get_problems_summary)
from submission.models import get_new_submission_id, add_submission, get_submissions_dict, get_mysubmissions_dict, get_submission_dict
from problem.models import get_problem_dict, get_problems_of_owner_id
# Create your views here.


def contests(request):
    context = {}

    context['CONTESTS'] = get_contests_dict(request.session.get('user_id'))

    if is_loggedin(request):
        context = add_user_information(request, context)
    return render(request, 'contest/contests.html', context)


def contest(request, contest_id):
    context = {}

    context = get_contest_dict(contest_id, request.session.get('user_id'))

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
    return render(request, 'contest/submission_view.html', context)


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


def register(request, contest_id):
    if not is_loggedin(request):
        return redirect('signin')
    add_participant(contest_id, request.session['user_id'])
    return redirect('contests')


def unregister(request, contest_id):
    if not is_loggedin(request):
        return redirect('signin')
    remove_participant(contest_id, request.session['user_id'])
    return redirect('contests')


def ask(request, contest_id):
    if is_loggedin(request) and request.method == 'POST':
        print(request.POST)
        question = request.POST['QUESTION']
        if question is not None and question != '':
            add_clarification_question(question, contest_id)
        return redirect('contest', contest_id)
    else:
        return redirect('contest', contest_id)


def remove_question(request, contest_id, clarification_id):
    if is_loggedin(request) and is_manager(contest_id, request.session['user_id']):
        remove_clarification_db(clarification_id, contest_id)
        return redirect('contest', contest_id)
    else:
        return redirect('contest', contest_id)


def update_question(request, contest_id, clarification_id):
    if is_loggedin(request) and is_manager(contest_id, request.session['user_id']) and request.method == 'POST':
        answer = request.POST['ANSWER']
        update_clarification(contest_id, clarification_id,  answer)
        return redirect('contest', contest_id)
    else:
        return redirect('contest', contest_id)


def add_problem(request, contest_id):
    if is_loggedin(request) and is_manager(contest_id, request.session['user_id']) and request.method == 'POST':
        problem_id = request.POST['PROBLEM_ID']
        alias = request.POST['ALIAS']
        add_problem_contest(contest_id, problem_id, alias)
        return redirect('contest', contest_id)
    else:
        return redirect('contest', contest_id)


def remove_problem(request, contest_id, problem_id):
    if is_loggedin(request) and is_manager(contest_id, request.session['user_id']):
        remove_problem_contest(contest_id, problem_id)
        return redirect('contest', contest_id)
    else:
        return redirect('contest', contest_id)


def show_problems_of_owner(request, contest_id):
    if is_loggedin(request) and is_manager(contest_id, request.session['user_id']):
        context = {}
        context['contest_id'] = contest_id
        owner_id = request.session['user_id']
        context = get_problems_of_owner_id(owner_id)
        return redirect('contest', context)
    else:
        return redirect('contest', contest_id)


def standings(request, contest_id):
    context = {}

    context = get_contest_dict(contest_id)

    context['PROBLEMS'] = get_problems_summary(contest_id)
    context['STANDINGS'] = get_standings_icpc_dict(contest_id)

    if is_loggedin(request):
        context = add_user_information(request, context)

    return render(request, 'contest/standings.html', context)
