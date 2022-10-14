from django.db import models
import uuid
from users.models import Profile
# Create your models here.

class Category(models.Model):
  name= models.CharField(verbose_name='名前', max_length=200)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  created =models.DateTimeField(verbose_name='登録日', auto_now_add=True)

  def __str__(self):
    return self.name

class Tag(models.Model):
  name= models.CharField(verbose_name='名前', max_length=200)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  created =models.DateTimeField(verbose_name='登録日', auto_now_add=True)

  def __str__(self):
    return self.name
  

class Site(models.Model):
  user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
  title = models.CharField(verbose_name='タイトル', max_length=200)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,verbose_name='カテゴリー')
  text = models.TextField(verbose_name='内容', null=True, blank=True)
  link = models.CharField(verbose_name='リンク', max_length=2000, null=True, blank=True)
  tags = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='タグ')
  vote_total = models.IntegerField(default=0, null=True, blank=True)
  vote_ratio = models.IntegerField(default=0, null=True, blank=True)
  created =models.DateTimeField(verbose_name='投稿日', auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  
  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ['-created']
    # ordering = ['-vote_ration', '-vote_total', 'title']
    
  @property
  def reviewers(self):
    queryset = self.review_set.all().values_list('owner__id', flat=True)
    return queryset
  
    
  @property
  def getVoteCount(self):
    reviews = self.review_set.all()
    upVotes = reviews.filter(value='up').count()
    totalVotes = reviews.count()
    ratio = (upVotes / totalVotes) * 100
    # print('totalVotes', totalVotes)
    # print('ratio', ratio)
    self.vote_total = totalVotes
    self.vote_ratio = ratio
    self.save()
    

class Review(models.Model):
  VOTE_TYPE = (
    ('up', '参考になる'),
    ('down', 'いまいち'),
      # ('Excellent', '大変有意義'),
      # ('Good', '参考になる'),
      # ('OK', '見る価値あり'),
      # ('Bad', '良くない'),
  )
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
  site = models.ForeignKey(Site, on_delete=models.CASCADE)
  body = models.TextField(verbose_name='感想（記述）', null=True, blank=True)
  value = models.CharField(verbose_name='感想（選択）', max_length=200, choices=VOTE_TYPE, blank=True)
  created =models.DateTimeField(verbose_name='作成日', auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  
  class Meta:
    unique_together = [['owner', 'site']]
  
  def __str__(self):
    return self.value
