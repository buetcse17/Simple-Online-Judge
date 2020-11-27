from django.urls import path

from . import views

urlpatterns = [
    path('', views.problemset, name='problemset'),
    path('submit/', views.submit, name='problemset_submit'),
    path('submit/<slug:alias>', views.submit,
         name='problemset_submit_problem'),
    path('problem/<slug:alias>', views.problem, name='problemset_problem'),
    path('my', views.mysubmissions, name='problemset_mysubmissions'),
    path('status', views.status, name='problemset_status'),
    path('submission/<int:submission_id>',
         views.submission, name='problemset_submission'),
]
