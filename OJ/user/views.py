from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import Http404

from .models import get_user_information, handle_exists, get_follower_count, is_loggedin, does_follow, get_institution_id, add_country
from .models import get_user_id, update_profile_picture_location, get_country_name, get_institution, get_institution_name, get_country_id
from .models import update_user_country, add_institution
from .models import update_user_institution

from OJ.utils import add_user_information
from django.core.files.storage import FileSystemStorage
from ratings.views import get_country

# Create your views here.


def profile(request, handle):
    if request.method == 'POST' and 'profilepic' in request.FILES:
        new_profilepic = request.FILES['profilepic']

        fs = FileSystemStorage()
        filename = fs.save(name=new_profilepic.name, content=new_profilepic)

        update_profile_picture_location(request.session['handle'], filename)

    if handle_exists(handle=handle):
        user_id, user_name,   rating, rating_catagory, color, country_id, country_name, institution_id, institution_name, profile_picture_location = get_user_information(
            handle=handle)

        context = {'handle': handle}

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
        context['total_follower'] = get_follower_count(user_id=user_id)

        if is_loggedin(request):
            context['does_follow'] = does_follow(
                user_id, request.session['user_id'])
            context = add_user_information(request=request, context=context)

        return render(request, 'user/profile.html', context=context)
    else:
        raise Http404('No such User')


def profile_settings(request):
    if is_loggedin(request):
        if request.method == 'POST':
            new_country = request.POST['country']
            new_institution = request.POST['institution']
            if new_country == '':
                new_country = None
            if new_institution == '':
                new_institution = None

            country_id = get_country_id(new_country)
            institution_id = get_institution_id(new_institution)

            if country_id is None and new_country is not None:
                add_country(new_country)
                country_id = get_country_id(country_name=new_country)
            if country_id is not None:
                update_user_country(request.session['handle'], country_id)

            if institution_id is None and new_institution is not None:
                add_institution(new_institution)
                institution_id = get_institution_id(
                    institution_name=new_institution)
            if institution_id is not None:
                update_user_institution(
                    request.session['handle'], institution_id)

        context = {'handle': request.session['handle']}

        context['countries'] = [y for x, y in get_country()]
        context['institutions'] = [y for x, y in get_institution()]
        context['current_country'] = get_country_name(
            handle=request.session['handle'])
        if (context['current_country'] is None):
            del context['current_country']

        context['current_institution'] = get_institution_name(
            handle=request.session['handle'])
        if (context['current_institution'] is None):
            del context['current_institution']

        context = add_user_information(request=request, context=context)
        return render(request, 'user/profile_settings.html', context=context)
    else:
        raise Http404('No such User')
