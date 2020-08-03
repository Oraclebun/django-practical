from django.db import models
import uuid

# Create your models here.


class Brand(models.Model):
    name = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.name


class Usage(models.Model):
    name = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(blank=False, max_length=50)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    desc = models.TextField(blank=False, max_length=200)
    origin = models.ForeignKey('Country', on_delete=models.CASCADE)
    weight_per_pack = models.FloatField(blank=False)
    qty_per_pack = models.IntegerField(blank=True, null=True)
    barcode_spec = models.CharField(blank=True, max_length=3)
    barcode_no = models.BigIntegerField(blank=True, null=True)
    image = models.URLField(blank=False)
    category = models.ManyToManyField('Category')
    usage = models.ManyToManyField('Usage')

    def __str__(self):
        return self.name


class ProductInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=False)
    expiry_date = models.DateField(blank=False)
    batch_no = models.IntegerField(blank=False)

    def __str__(self):
        return self.product.name

