from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Categorie, Subscription, Post

# Create your views here.
def subscribe(request):
	if request.method == "POST":
		subscriber = request.POST['subscriber']

		if Subscription.objects.filter(subscriber=subscriber).exists():
			messages.warning(request, "Error! The email {}, has been subscribed. Try another one.".format(subscriber))
			return redirect('about:home')
		else:
			new_subscription = Subscription(subscriber=subscriber).save()

			messages.success(request, "Success! You have been successfully subscribed to our blog.")
			return redirect('about:home')
	else:
		messages.warning(request, "Error! You were not subscribed.")
		return redirect('about:home')

def blog_posts(request):
	posts = Post.objects.all()
	context = {
		'posts' : posts,
	}
	return render(request, "blog/index.html", context)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	posts = Post.objects.all()

	context = {
		'post' : post,
		'posts' : posts,
	}

	return render(request, "blog/post.html", context)

