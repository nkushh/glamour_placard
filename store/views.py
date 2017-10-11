from .models import Product_categorie, Sub_categorie, Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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



# Add new item category
@login_required(login_url='login')
def new_category(request):
	if request.method == "POST":
		category_name = request.POST['category_name']

		if not(Product_categorie.objects.filter(category_name=category_name).exists()):
			category = Product_categorie(category_name=category_name).save()
			messages.success(request, "Success! {} category details successfully recorded.".format(category_name))
			return redirect('store:item_categories')
		else:
			messages.error(request, "Error! {} category name already exists. Try another.".format(category_name))
			return redirect('store:item_categories')
	else:
		return redirect('store:item_categories')

# Fetch all item categories
@login_required(login_url='login')
def item_categories(request):
	categories = Product_categorie.objects.all().order_by('-created_on')

	context = {
		'categories' : categories,
	}

	return render(request, "dashboard/item-categories.html", context)

# Delete item category
@login_required(login_url='login')
def delete_category(request, category_id):
	category = get_object_or_404(Product_categorie, pk=category_id)
	category.delete()
	messages.success(request, "Success! Category details have been deleted.")
	return redirect('store:item_categories')


# Fetches sub-categories of an item category
@login_required(login_url='login')
def all_subcategories(request, category_id):
	category = get_object_or_404(Product_categorie, pk=category_id)
	categories = Sub_categorie.objects.filter(category=category).order_by('-created_on')

	context = {
		'categories' : categories,
	}

	return render(request, "dashboard/sub-categories.html", context)



# Fetch all items in the database. Order by date added
@login_required(login_url='login')
def all_items(request):
	items = Product.objects.all().order_by('-added_on')

	context = {
		'items' : items,
	}

	return render(request, "dashboard/items.html", context)
