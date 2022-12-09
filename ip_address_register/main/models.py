from django.db import models

# Create your models here.

class ServerAddress(models.Model):
    serverType = models.CharField(max_length=200, null=False)
    serverURL = models.URLField(max_length=200, null=False)
    
