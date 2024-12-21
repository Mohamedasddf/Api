from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer,UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        # استخدام السيريالايزر للتحقق من البيانات
        serializer = self.get_serializer(data=request.data)
        
        # التحقق من صحة البيانات
        if serializer.is_valid():
            user = serializer.save()  # حفظ المستخدم
        else:
            # إرجاع الأخطاء إذا كانت البيانات غير صالحة
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # إنشاء التوكن للمستخدم الجديد
        token, created = Token.objects.get_or_create(user=user)

        # إرجاع التوكن فقط
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)



class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {
            'message': 'This is not how you should create or update'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
