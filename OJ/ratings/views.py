from django.shortcuts import render

from user.models import get_country , get_institution
from .models import get_ratings
# Create your views here.

def ratings(request):
    context = {}
    
    context['users'] = get_ratings()
    context['countries'] =  get_country()
    context['institutions'] = get_institution()

    return render(request , 'ratings.html' , context=context)