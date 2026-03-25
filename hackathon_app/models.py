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
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        # tutorial man uses "_create_user()" and "create_user()" and they're two different functions so watch out
        if not email:
            raise ValueError('no valid email provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class Generic_User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    first_name = models.CharField(blank=True, default='', max_length=32)
    last_name = models.CharField(blank=True, default='', max_length=32)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_last_name(self):
        return self.last_name


# Admin class
class admin(Generic_User):
    objects = CustomUserManager()

    admin_id = models.AutoField(blank=True, primary_key=True)
    admin_first_name = models.TextField(blank=True, null=True, max_length=32)  # This may be redundant
    admin_last_name = models.TextField(blank=True, null=True, max_length=32)  # This may be redundant
    admin_email = models.TextField(blank=True, null=True, max_length=64)  # This may be redundant

    class Meta:
        db_table = 'admin'



# end user class
class endUser(Generic_User):
    objects = CustomUserManager()

    user_id = models.AutoField(blank=True, primary_key=True)
    user_first_name = models.TextField(blank=True, null=True, max_length=32)  # This may be redundant
    user_last_name = models.TextField(blank=True, null=True, max_length=32)  # This may be redundant
    user_email = models.TextField(blank=True, null=True, max_length=64)  # This may be redundant

    class Meta:
        db_table = 'endUser'

"""