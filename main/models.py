from django.db import models
from django.contrib.auth.models import User,AbstractUser


class User(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)

     
    class Meta(AbstractUser.Meta):
        swappable ='AUTH_USER_MODEL'
        verbose_name='User'
        verbose_name_plural='Users'
    
    
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=9,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)

class Comment(models.Model):
    comment = models.TextField()

    class Meta:
        ordering = ('comment',)
