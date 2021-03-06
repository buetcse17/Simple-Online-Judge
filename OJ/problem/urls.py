from django.urls import path

from . import views

urlpatterns = [
    path('', views.problems, name='problems'),
    path('edit/<int:problem_id>/', views.problem_edit, name='problem_edit'),
    path('view/<int:problem_id>/', views.problem_view, name='problem_view'),
    path('add_sample/<int:problem_id>/', views.add_sample, name='problem_add_sample'),
    path('remove_sample/<int:problem_id>/<int:sample_testcase_id>', views.remove_sample, name='problem_remove_sample'),
    path('remove/<int:problem_id>', views.problem_remove, name='problem_remove'),
]
