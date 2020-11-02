from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect

from user.models import is_loggedin , get_user_id
from follow.models import AddFollower , RemoveFollower
# Create your views here.

def AddFriend(request , friend_user_id):
    if is_loggedin(request=request):
        AddFollower(followee_id= friend_user_id , follower_id= get_user_id(request.session['handle']) )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('signin')

def RemoveFriend(request , friend_user_id):
    if is_loggedin(request=request):
        RemoveFollower(followee_id= friend_user_id , follower_id= get_user_id(request.session['handle']) )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('signin')
        