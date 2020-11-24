from django.urls import path

from . import views

urlpatterns = [
    path('', views.submissions, name='submissions'),
    path('<hndl:handle>', views.submissions_user, name='submissions_user'),
]
