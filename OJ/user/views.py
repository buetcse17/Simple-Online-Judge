from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import Http404

from .models import get_user_information , handle_exists , get_follower_count , is_loggedin , does_follow , get_user_id
from OJ.utils import add_user_information

# Create your views here.
def profile(request , handle):
    if handle_exists(handle= handle):
        user_id , user_name ,   rating , rating_catagory ,color , country_id , country_name ,institution_id , institution_name , profile_picture_location  = get_user_information(handle=handle)

        context = { 'handle': handle}

        context['user_id'] = user_id
        context['user_name'] = user_name
        context['rating'] = rating
        context['rating_catagory'] = rating_catagory
        context['color'] = color
        context['country_id'] = country_id
        context['country_name'] = country_name
        context['institution_id'] = institution_id
        context['institution_name'] = institution_name
        context['profile_picture_location'] = profile_picture_location
        context['total_follower'] = get_follower_count(user_id = user_id)

        if is_loggedin(request):
            context['does_follow'] = does_follow(user_id , request.session['user_id'])
            context = add_user_information(request= request , context= context)

        return render(request , 'profile.html' , context=context )
    else :
        raise Http404('No such User')

def profile_settings(request):
    print('here runs')
    print(request.session['handle'])
    if is_loggedin(request):

        context = { 'handle': request.session['handle']}
        return render(request , 'profile_settings.html' , context=context )
    else:
        raise Http404('No such User')