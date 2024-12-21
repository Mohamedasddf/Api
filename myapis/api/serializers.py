from rest_framework import serializers
from .models import Meal, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')  # فقط اسم المستخدم وكلمة المرور
        extra_kwargs = {
            'password': {'write_only': True}  # اجعل كلمة المرور للكتابة فقط
        }


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'meal')        