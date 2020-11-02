from django.urls import path, register_converter

from . import views

urlpatterns = [
    path('add/<int:friend_user_id>',views.AddFriend, name = 'AddFriend'),
    path('remove/<int:friend_user_id>',views.RemoveFriend, name = 'RemoveFriend'),
]