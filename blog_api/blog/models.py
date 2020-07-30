from django.db import models
from django.utils import timezone
from userinfo.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    statuses = [
        ("D", "Draft"),
        ("P","Publish"),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices = statuses)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/post', blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


