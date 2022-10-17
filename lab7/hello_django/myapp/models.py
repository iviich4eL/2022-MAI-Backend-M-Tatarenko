from ssl import create_default_context
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Creator(models.Model):
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField()

class Post(models.Model):
    user = models.ForeignKey(Creator, on_delete=models.CASCADE)
    headline = models.CharField(max_length=30, blank=False, null=False)
    content = models.CharField(max_length=300, blank=False, null=False)
    created_at = models.DateField()