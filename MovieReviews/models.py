from django.db import models
from django.conf import settings

# Create your models here.
class Showings(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    showing = models.ForeignKey(Showings, on_delete=models.CASCADE)
    review_text = models.TextField()
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review for {self.showing.title} by {self.reviewer.username}"
    
class Ratings(models.Model):
    showing = models.ForeignKey(Showings, on_delete=models.CASCADE)
    rating_value = models.IntegerField()
    