from django.urls import path

from . import views

urlpatterns = [
    path('<slug:handle>/', views.profile, name='profile'),
]