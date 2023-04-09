from django.contrib import admin
from .models import Product, ProductCategory

# Register your models here.

class Productcategoryadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class Productadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Product, Productadmin)

admin.site.register(ProductCategory, Productcategoryadmin)