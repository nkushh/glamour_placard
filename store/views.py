from .models import Product_categorie, Sub_categorie, Product
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def all_products(request):
	products = Product.objects.all().order_by('-added_on')

	context = {
		'products' : products,
	}

	return render(request, "store/index.html", context)


def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)

	context = {
		'product' : product,
	}

	return render(request, "store/product.html", context)
