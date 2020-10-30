from django.urls import path

from . import views

urlpatterns = [
    path('', views.ratings, name='ratings'),
    path('country/<int:country_id>',views.country_ratings , name = 'country_rating'),
    path('institution/<int:institution_id>',views.institution_ratings , name = 'institution_rating')
]