from django.db import models

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


class BusinessOrganization(models.Model):
    id = models.IntegerField(primary_key=True)
    business_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'business_organization'


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
    user = models.ForeignKey(AuthUser)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    business_name = models.TextField(blank=True)
    logo = models.TextField(blank=True)
    about = models.TextField(blank=True)
    website = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    country = models.ForeignKey(Country)
    class Meta:
        db_table = 'enterprise_business'
