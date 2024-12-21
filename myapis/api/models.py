from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    meal = models.ForeignKey(Meal, related_name='meal', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

   # class Meta:
        # يمنع تكرار البيانات عن طريق منع المستخدم من تقييم نفس الوجبة أكثر من مرة.
      #  unique_together = (('user', 'meal'),)
        #يحسن أداء استعلامات قاعدة البيانات عندما تحتاج إلى البحث عن تقييمات بناءً على user و meal في نفس الوقت.
      #  indexes = [
      #      models.Index(fields=['user', 'meal']),
      #  ]
