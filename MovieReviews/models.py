from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Showing(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField()
    duration = models.CharField(max_length=20)
    showing_date = models.DateField(default=timezone.now)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    poster_image = models.URLField()
    #professional_review_link = models.URLField()

    def when_selected(self):
        return self.title
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    showing = models.ForeignKey('MovieReviews.Showing', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review for {self.showing.title} by {self.reviewer.username}, /'{self.review_text}/'"    