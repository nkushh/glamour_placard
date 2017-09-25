from django.db import models

# Create your models here.
class Product_categorie(models.Model):
	category_name = models.CharField(max_length=200)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category_name

class Sub_categorie(models.Model):
	category = models.ForeignKey(Product_categorie)
	sub_category = models.CharField(max_length=200)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.sub_category


class Product(models.Model):
	category = models.ForeignKey(Product_categorie)
	sub_category = models.ForeignKey(Sub_categorie)
	product_name = models.CharField(max_length=200)
	color = models.CharField(max_length=200, blank=True)
	price = models.FloatField()
	size = models.CharField(max_length=200, blank=True)
	description = models.TextField(blank=True)
	product_img = models.ImageField(upload_to='store')
	availability_status = models.IntegerField(default=0)
	added_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product_name

