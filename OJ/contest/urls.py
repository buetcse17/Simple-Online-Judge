from django.urls import path

from . import views

urlpatterns = [
    path('', views.contests, name='contests'),
    path('<int:contest_id>', views.contest, name='contest'),
]