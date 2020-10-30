from django.shortcuts import render

from user.models import get_country , get_institution
from .models import get_ratings , get_country_ratings , get_institution_ratings
# Create your views here.

def ratings(request):
    context = {}
    
    context['users'] = get_ratings()
    context['countries'] =  get_country()
    context['institutions'] = get_institution()

    return render(request , 'ratings.html' , context=context)
def country_ratings(request , country_id):
    context = {}
    context['users'] = get_country_ratings(country_id=country_id)
    context['countries'] =  get_country()
    context['institutions'] = get_institution()
    context['selected_country'] = country_id 
    try:
        del context['selected_institution']
    except:
        pass

    return render(request , 'ratings.html' , context=context)

def institution_ratings(request , institution_id):
    context = {}
    context['users'] = get_institution_ratings(institution_id=institution_id)
    context['countries'] =  get_country()
    context['institutions'] = get_institution()
    context['selected_institution'] = institution_id 
    try:
        del context['selected_country']
    except:
        pass

    return render(request , 'ratings.html' , context=context)


