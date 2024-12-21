from django.contrib import admin
from . models import User, Meal, Rating
# Register your models here.
admin.site.register(Meal)
admin.site.register(Rating)