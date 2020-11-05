from django.shortcuts import render
from django.http import Http404
from user.models import get_country, get_institution
from .models import get_ratings, get_country_ratings, get_institution_ratings, country_exists, institution_exists
from OJ.utils import add_user_information
from user.models import is_loggedin
# Create your views here.


def ratings(request):
    context = {}

    context['users'] = get_ratings()
    context['countries'] = get_country()
    context['institutions'] = get_institution()

    if is_loggedin(request):
        context = add_user_information(request= request , context = context)

    return render(request, 'ratings.html', context=context)


def country_ratings(request, country_id):

    if not country_exists(country_id=country_id):
        raise Http404('No such Country')
    else:
        context = {}
        context['users'] = get_country_ratings(country_id=country_id)
        context['countries'] = get_country()
        context['institutions'] = get_institution()
        context['selected_country'] = country_id
        try:
            del context['selected_institution']
        except:
            pass
        
        if is_loggedin(request):
            context = add_user_information(request= request , context = context)


        return render(request, 'ratings.html', context=context)


def institution_ratings(request, institution_id):
    if not institution_exists(institution_id=institution_id):
        raise Http404('No such Country')
    else:
        context = {}
        context['users'] = get_institution_ratings(
            institution_id=institution_id)
        context['countries'] = get_country()
        context['institutions'] = get_institution()
        context['selected_institution'] = institution_id
        try:
            del context['selected_country']
        except:
            pass
        
        if is_loggedin(request):
            context = add_user_information(request= request , context = context)

        return render(request, 'ratings.html', context=context)
