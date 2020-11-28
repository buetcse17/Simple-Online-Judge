from django.urls import path

from . import views

urlpatterns = [
    path('', views.contests, name='admin_contests'),
    path('add_contest', views.add_contest, name='admin_add_contest'),
]
