from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin

# Create your models here.
class user_table  (models.Model):
    user_id = models.AutoField(primary_key=True)
    user_username = models.TextField(null=False)
    user_email = models.TextField(blank = True)
    class Meta:
        db_table = 'user_table'

class products_list(models.Model):
    products_list_id = models.AutoField(primary_key=True)
    product_label = models.TextField(max_length=5)
    product_description = models.TextField(blank=True)
    class Meta:
        db_table = 'products_list'



class sales(models.Model):
    stock_id = models.AutoField(primary_key=True)
    store_id = models.TextField(max_length=4)
    product_label = models.TextField(max_length=5)
    category = models.TextField(max_length=20)
    region = models.TextField(max_length=5)
    inventory_level = models.IntegerField()
    units_sold = models.IntegerField()
    units_ordered = models.IntegerField()
    price = models.FloatField()
    discount = models.IntegerField()
    weather_condition = models.TextField()
    promotion = models.IntegerField()
    competitor_pricing = models.FloatField()
    seasonality = models.TextField()
    epidemic = models.IntegerField()
    demand = models.IntegerField()
    class Meta:
        db_table = 'sales_data'



""" Old Sales Model
class sales(models.Model):
    stock_id = models.AutoField(primary_key=True)
    store_id = models.TextField(max_length=4)
    product_id = models.TextField(max_length=5)
    category = models.TextField(max_length=20)
    region = models.TextField(max_length=5)
    inventory_level = models.IntegerField()
    units_sold = models.IntegerField()
    units_ordered = models.IntegerField()
    price = models.FloatField()
    discount = models.IntegerField()
    weather_condition = models.TextField()
    promotion = models.IntegerField()
    competitor_pricing = models.FloatField()
    seasonality = models.TextField()
    epidemic = models.IntegerField()
    demand = models.IntegerField()
    class Meta:
        db_table = 'sales_data'
"""