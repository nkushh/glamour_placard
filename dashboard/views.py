from blog.models import Categorie, Post
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Categorie, Subscription, Post
from store.models import Product_categorie, Sub_categorie, Product

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
	return render(request, 'dashboard/index.html')

# Accounts CRUD functions

# @login_required(login_url='login')
# def new_account(request):
#     return render(request, 'dashboard/add-user.html')


# @login_required(login_url='login')
# def create_account(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email =  request.POST['email']
#         password =  request.POST['password']

#         if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
#             User.objects.create_user(username, email, password)
#             messages.success(request, "Success! Account detail successfully recorded.")
#         else:
#         	messages.warning(request, "Error! Looks like a username with that email or password already exists.")
#     else:
#     	return render(request, 'dashboard/create-account.html')




# End of Accounts CRUD functions




