from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class DecoUser(AbstractUser):
    karma = models.PositiveIntegerField(_("karma"),
        default=0,blank=True)



'''
# Create your models here.
class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'
    
    def __unicode__(self):
        return self.username    
'''

class BusinessType(models.Model):
    id = models.IntegerField(primary_key=True)
    business_type_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'business_type'
    
    def __unicode__(self):
        return self.business_type_name
    

class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = 'country'
    
    def __unicode__(self):
        return self.country_name
    
    


class EnterpriseBusiness(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User)
    business_type = models.ForeignKey(BusinessType, null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    business_name = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to="images/logos", max_length=255, blank=True)
    about = models.TextField(blank=True)
    website = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)

    def __str__(self):  
          return '%s profile' % self.user
    
    class Meta:
        db_table = 'enterprise_business'



'''
class MyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True, db_index=True)
    date_of_birth = models.DateTimeField()
    height = models.FloatField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['date_of_birth', 'height']
'''
