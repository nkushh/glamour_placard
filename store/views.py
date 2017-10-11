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
	categoriess = Product_categorie.objects.all()
	categories = Sub_categorie.objects.filter(category=get_object_or_404(Product_categorie, pk=category_id)).order_by('-created_on')

	context = {
		'categoriess' : categoriess,
		'categories' : categories,
	}

	return render(request, "dashboard/sub-categories.html", context)

@login_required(login_url='login')
def new_subcategory(request):
	if request.method == "POST":
		category = get_object_or_404(Product_categorie, pk=request.POST['category'])
		sub_category = request.POST['sub_category']

		if not(Sub_categorie.objects.filter(sub_category=sub_category).exists()):
			category = Sub_categorie(category=category, sub_category=sub_category).save()
			messages.success(request, "Success! {} category details successfully recorded.".format(sub_category))
			return redirect('store:sub_categories', category_id=request.POST['category'])
		else:
			messages.error(request, "Error! {} category name already exists. Try another.".format(category_name))
			return redirect('store:sub_categories', category_id=request.POST['category'])
	else:
		return redirect('store:item_categories')



# Fetch all items in the database. Order by date added
@login_required(login_url='login')
def all_items(request):
	items = Product.objects.all().order_by('-added_on')

	context = {
		'items' : items,
	}

	return render(request, "dashboard/items.html", context)


# Render template to add new item
@login_required(login_url='login')
def new_item(request):
	categories = Sub_categorie.objects.all()

	context = {
		'categories' : categories,
	}

	return render(request, "dashboard/new-item.html", context)

@login_required(login_url='login')
def add_item(request):
	if request.method=="POST":
		sub_category = get_object_or_404(Sub_categorie, pk=request.POST['category'])
		category = sub_category.category
		product_name = request.POST['product_name']
		color = request.POST['color']
		price = request.POST['price']
		size = request.POST['size']
		stock = request.POST['stock']
		description = request.POST['description']
		if len(request.FILES) > 0:
			product_img = request.FILES['product_img']

		if Product.objects.filter(product_name=product_name).exists():
			messages.error(request, "Error! A product with name '{}' already exists. Try another".format(product_name))
			return redirect('store:new_item')
		else:
			if len(request.FILES) > 0:
				item = Product(category=category, sub_category=sub_category, product_name=product_name, color=color, price=price, description=description, stock=stock, product_img=product_img)
			else:
				item = Product(category=category, sub_category=sub_category, product_name=product_name, color=color, price=price, description=description, stock=stock)

			item.save()
			messages.success(request, "Success! Item {} details have been saved".format(product_name))
			return redirect('store:all_items')
	else:
		return redirect('store:new_item')
