from django.urls import path, register_converter

from . import views

urlpatterns = [
    path('',views.messages, name = 'messages'),
    path('with/<hndl:handle>',views.conversation, name = 'conversation'),
]