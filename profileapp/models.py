from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    ## user 랑 Profile을 1대1매칭 on_delete 는 user 가 사라지면 프로필도 사라짐 
    ## realated_name 은 request.user.profile.nickname 이런식으로 연결해줌 
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name = 'profile') 

    image = models.ImageField(upload_to='profile/',null=True)
    nickname = models.CharField(max_length=20 , unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

    
