from django.db import models

# Create your models here.

class Categorie(models.Model):
	category_name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category_name


class Post(models.Model):
	category = models.ForeignKey(Categorie)
	post_title = models.CharField(max_length=200)
	post_content = models.TextField()
	featured_img = models.ImageField(upload_to='posts')
	author = models.ForeignKey('auth.User')
	created_on = models.DateTimeField(auto_now_add=True)
	published_on = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.post_title

class Subscription(models.Model):
	subscriber = models.EmailField()
	subscription_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.subscriber
