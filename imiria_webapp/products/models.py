from django.db import models

# Create your models here.

class ImiriaCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    category_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'imiria_category'


class ImiriaProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(ImiriaCategory, null=True, blank=True)
    class Meta:
        db_table = 'imiria_product'




