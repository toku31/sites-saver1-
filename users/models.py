from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ユーザー',null=True, blank=True)
  name = models.CharField(verbose_name='名前', max_length=200, blank=True, null=True)
  email = models.EmailField(verbose_name='メール', max_length=500, blank=True, null=True)
  username = models.CharField(verbose_name='ユーザ名', max_length=200, blank=True, null=True)
  location = models.CharField(verbose_name='住所', max_length=200, blank=True, null=True)
  short_intro = models.CharField(verbose_name='挨拶文', max_length=200, blank=True, null=True)
  bio = models.TextField(verbose_name='自己紹介', blank=True, null=True)
  profile_image = models.ImageField(verbose_name='画像',blank=True, null=True, default="user-default.png")
  social_github = models.CharField(verbose_name='Github', max_length=200, blank=True, null=True)
  social_website = models.CharField(verbose_name='Website', max_length=200, blank=True, null=True)
  # social_twitter = models.CharField(max_length=200, blank=True, null=True)
  # social_youtube = models.CharField(max_length=200, blank=True, null=True)
  created =models.DateTimeField(verbose_name='作成日', auto_now_add=True)
  id = models.UUIDField(verbose_name='ID', default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  
  def __str__(self):
    return str(self.user.username)
  


    
  