from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Tweet(models.Model):
    status = models.CharField(max_length=280)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.status)
                               