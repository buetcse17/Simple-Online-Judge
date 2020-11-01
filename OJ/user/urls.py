from django.urls import path, register_converter

from . import views

class HandleURL:
    regex = '[\S]*'

    def to_python(self , value):
        return str(value)
    
    def to_url(self , value):
        return str(value)

register_converter(HandleURL, 'hndl')

urlpatterns = [
    path('<hndl:handle>/', views.profile, name='profile'),
    path('<hndl:handle>/profile_settings/',views.profile_settings, name = 'profile'),
]