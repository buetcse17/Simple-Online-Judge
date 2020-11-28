from django.urls import path

from . import views

urlpatterns = [
    path('', views.contests, name='admin_contests'),
]
