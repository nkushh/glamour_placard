from django.shortcuts import render
from blog.models import Post
from store.models import Product

# Create your views here.
def home(request):
	posts = Post.objects.all()[:4]
	products = Product.objects.all()
	context = {
		'posts' : posts,
		'products' : products,
	}
	return render(request, 'about/index.html', context)