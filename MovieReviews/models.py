from django.db import models
from django.conf import settings

# Create your models here.
class Showing(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField()
    duration = models.CharField(max_length=20)
    release_date = models.DateField()

    def when_selected(self):
        return self.title
    


    def __str__(self):
        return self.title
    
class Review(models.Model):
    showing = models.ForeignKey(Showing, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    #created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review for {self.showing.title} by {self.reviewer.username}"
    
class ProfessionalReview(models.Model):
    showing = models.ForeignKey(Showing, on_delete=models.CASCADE)
    critic_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    publication = models.CharField(max_length=100)

    def __str__(self):
        return f"Professional Review for {self.showing.title} by {self.critic_name}"  
    

    