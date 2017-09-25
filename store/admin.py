from django.contrib import admin

from .models import Product_categorie, Sub_categorie, Product

# Register your models here.
admin.site.register(Product_categorie)
admin.site.register(Sub_categorie)
admin.site.register(Product)
