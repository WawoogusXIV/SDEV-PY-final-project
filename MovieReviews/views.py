from django.shortcuts import render, get_object_or_404
from .models import Showing, Review
from django.utils import timezone
from django.shortcuts import redirect
from .forms import ReviewForm

# Create your views here.

def home_page(request):
    show = Showing.objects.all()

    return render(request, 'showings/posters.html', {'show': show})

def movie_page(request, pk):
    this_post = get_object_or_404(Showing, pk=pk)
    reviews = this_post.review_set.all().order_by('-created_at')
    return render(request, 'showings/movie_details.html', {'this_post': this_post, 'reviews': reviews})

def new_review(request, pk):
    this_post = get_object_or_404(Showing, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.showing = this_post
            review.created_at = timezone.now()
            review.save()
            return redirect('movie_page', pk=this_post.pk)
    else:
        form = ReviewForm()
    
    return render(request, 'showings/new_review.html', {'form': form, 'this_post': this_post})