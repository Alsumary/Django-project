# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManage(AbstractUser, models.Model):
  role = models.CharField(max_length=20)
  pass

class category(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField(max_length=500)
  image = models.CharField(max_length=2000)

class articles(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField(max_length=500)
  image = models.CharField(max_length=2000)
  category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="article_category")
  isActive = models.BooleanField(default=False)
  articleTime = models.TimeField()
  articleDate = models.DateField()
  createdAt = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
        return f"{self.title}"
      
class comments(models.Model):
  content = models.TextField(max_length=500)
  article = models.ForeignKey(articles, on_delete=models.CASCADE, related_name="comment_article")
  user = models.ForeignKey(UserManage, on_delete=models.CASCADE, related_name="comment_user")
  
  def __str__(self):
    return f"{self.content}"

class subscriptions(models.Model):
  user = models.ForeignKey(UserManage, on_delete=models.CASCADE, related_name="subscription_user")
  category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="subscription_category")
