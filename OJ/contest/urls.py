from django.urls import path

from . import views

urlpatterns = [
    path('', views.contests, name='contests'),
    path('<int:contest_id>', views.contest, name='contest'),
    path('<int:contest_id>/submit', views.submit, name='submit'),
    path('<int:contest_id>/submit/<slug:alias>',
         views.submit, name='submit_problem'),
    path('<int:contest_id>/my', views.mysubmissions, name='mysubmissions'),
    path('<int:contest_id>/status', views.status, name='status'),
    path('<int:contest_id>/submission/<int:submission_id>',
         views.submission, name='submission'),
    path('<int:contest_id>/problem/<slug:alias>', views.problem, name='problem'),
    path('<int:contest_id>/register>', views.register, name='contest_register'),
    path('<int:contest_id>/unregister>',
         views.unregister, name='contest_unregister'),
    path('<int:contest_id>/ask>', views.ask, name='contest_ask'),
    path('<int:contest_id>/remove_question/<int:clarification_id>',
         views.remove_question, name='contest_remove_question'),
    path('<int:contest_id>/update_question/<int:clarification_id>',
         views.update_question, name='contest_update_question'),
]
