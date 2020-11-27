from django.urls import path

from . import views

urlpatterns = [
    path('ad/', views.admin, name='admin'),
]
