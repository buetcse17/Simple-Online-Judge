from django.urls import path

from . import views

urlpatterns = [
    path('', views.problems, name='problems'),
    path('edit/<int:problem_id>', views.problem_edit, name='problem_edit'),
]
