from django.contrib import admin
from .models import Subscription, Categorie, Post

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Categorie)
admin.site.register(Post)
