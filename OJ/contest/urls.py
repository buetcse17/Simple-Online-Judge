from django.urls import path

from . import views

urlpatterns = [
    path('', views.contests, name='contests'),
    path('<int:contest_id>', views.contest, name='contest'),
    path('<int:contest_id>/submit', views.submit, name='submit'),
    path('<int:contest_id>/submit/<slug:alias>', views.submit, name='submit_problem'),
    path('<int:contest_id>/mysubmissions', views.mysubmissions, name='mysubmissions'),
]