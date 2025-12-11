from django.shortcuts import render
from .models import Showing
from django.utils import timezone

# Create your views here.

def home_page(request):
    show = Showing.objects.all()

    return render(request, 'showings/posters.html', {'show': show})

def movie_page(request):
    return render(request, 'showings/MoviePage.html', {})