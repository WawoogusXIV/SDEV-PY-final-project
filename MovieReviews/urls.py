from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),

    path('MoviePage', views.movie_page, name='movie_page')
]