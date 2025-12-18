from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),

    path('<int:pk>', views.movie_page, name='movie_page'),

    path('<int:pk>/new-review', views.new_review, name='new_review'),

]