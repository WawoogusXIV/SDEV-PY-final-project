from django.contrib import admin
from .models import Showings, Reviews, Ratings

# Register your models here.
admin.site.register(Showings)
admin.site.register(Reviews)
admin.site.register(Ratings)