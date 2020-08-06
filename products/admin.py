from django.contrib import admin
from .models import Brand,Country,Category,Product,Usage

# Register your models here.
admin.site.register(Brand)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Usage)
