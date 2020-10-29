from django.shortcuts import render

from .models import get_ratings
# Create your views here.

def ratings(request):
    sql_result = get_ratings()
    print(sql_result)
    context = {}
    context['users'] = []
    for handle , total_contest_participation , rating in sql_result:
        user  = { "handle":handle ,
                "total_contest_participation" : total_contest_participation , 
                "rating":rating ,
                }
        context['users'].append(user)
    return render(request , 'ratings.html' , context=context)