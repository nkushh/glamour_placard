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





