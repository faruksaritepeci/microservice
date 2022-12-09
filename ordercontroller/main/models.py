from django.db import models
from enum import Enum

# Create your models here.
class OrderStatus(models.IntegerChoices): # ENUM
    Created = 10, "Created"
    InProgress = 20, "InProgress"
    Failed = 30, "Failed"
    Completed = 40, "Completed"
    Canceled = 50, "Canceled"
    Returned = 60, "Returned"


class Order(models.Model):
    # id is already added by superclass
    # OwnerUser = models.IntegerField() # To track the user id that owns the order post
    # removed for this assignment
    
    ItemId = models.IntegerField(null=False)
    BrandId = models.IntegerField()
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    StoreName = models.CharField(max_length=200)
    CustomerName = models.CharField(max_length=200)
    CreatedOn = models.DateTimeField()
    Status = models.IntegerField(choices=OrderStatus.choices)


class OrderFilterModel(models.Model):
    
    PageSize = models.IntegerField(default=10)
    
    PageNumber = models.IntegerField(default=1)
    
    SearchText = models.CharField(max_length=200)
    
    StartDate = models.DateTimeField()
    
    EndDate = models.DateTimeField()
    
    Statuses = models.JSONField() # List of statuses
    
    SortBy = models.CharField(max_length=200)
    