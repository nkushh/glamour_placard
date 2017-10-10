from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
	posts = Post.objects.filter(published_on__isnull=False).order_by('-published_on')
	context = {
		'posts' : posts,
	}
	return render(request, "blog/index.html", context)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	posts = Post.objects.filter(published_on__isnull=False).order_by('-published_on')[:3]

	context = {
		'post' : post,
		'posts' : posts,
	}

	return render(request, "blog/post.html", context)


# BEGIN BLOG CRUD FUNCTIONS
# Fetches all blog categories from teh database
@login_required(login_url='login')
def blog_categories(request):
	context = {
		'categories' : Categorie.objects.all(),
	}
	return render(request, "dashboard/post-categories.html", context)

# Adds a new blog category to the database and launches the form for the category details
@login_required(login_url='login')
def register_category(request):
	if request.method=="POST":
		category_name = request.POST['category_name']

		if Categorie.objects.filter(category_name=category_name).exists():
			messages.error(request, "Error! {} blog category already exists. Try another name".format(category_name))
			return redirect('blog:blog_categories')
		else:
			new_category = Categorie(category_name=category_name).save()
			messages.success(request, "Success! {} blog category has been added.".format(category_name))
			return redirect('blog:blog_categories')
	else:
		return redirect('blog:blog_categories')

@login_required(login_url='login')
def edit_blog_category(request, category_id):
	category = get_object_or_404(Categorie, pk=category_id)

	context = {
		'category' : category,
	}
	return render(request, "dashboard/edit-blog-category.html", context)

# Fetches details of a particular blog category for editing and launches the form  for the same
@login_required(login_url='login')
def update_blog_category(request, category_id):
	category = get_object_or_404(Categorie, pk=category_id)
	if request.method=="POST":
		category_name = request.POST['category_name']
		category.category_name = category_name
		category.save()
		messages.success(request, "Success! Category name successfuly updated.")
		return redirect('blog:blog_categories')
	else:
		messages.success(request, "Error! Category name wasn't updated.")
		return redirect('blog:edit_category', category_id=category.pk)

# Fetches a particular blog category and its details from the database
@login_required(login_url='login')
def blog_category_details(request, category_id):
	category = get_object_or_404(Categorie, pk=category_id)
	context = {
		'category' : category,
	}
	return render(request, "dashboard/category.html", context)

@login_required(login_url='login')
def delete_blog_category(request, category_id):
	category = get_object_or_404(Categorie, pk=category_id)
	category.delete()
	messages.success(request, "Success! Category details successfully deleted!")
	return redirect("dashboard:blog_categories")

# Fetches all the blog posts in the database
@login_required(login_url='login')
def view_posts(request):
	context = {
		'posts' : Post.objects.all().order_by('-created_on'),
	}
	return render(request, "dashboard/posts.html", context)


@login_required(login_url='login')
def new_post(request):
	context = {
		'categories' : Categorie.objects.all(),
	}

	return render(request, "dashboard/new-post.html", context)


# Function to get published blogs only
# @login_required(login_url='login')
# def published_blog_posts(request):
# 	context = {
# 		'posts' : Post.objects.filter(date_published__isnull=False).order_by('-date_published'),
# 	}
# 	return render(request, "dashboard/blog_posts.html", context)

# Function to get draft blogs only
# @login_required(login_url='login')
# def draft_blog_posts(request):
# 	context = {
# 		'posts' : Post.objects.filter(date_published__isnull=True).order_by('-date_created'),
# 	}
# 	return render(request, "dashboard/blog_posts.html", context)

# Function to get blog post details
# @login_required(login_url='login')
# def post_details(request, post_id):
# 	context = {
# 		'post' : get_object_or_404(Post, pk=post_id)
# 	}
# 	return render(request, "dashboard/post_details.html", context)

@login_required(login_url='login')
def post_details(request, post_id):
	blog_post = get_object_or_404(Post, pk=post_id)

	context = {
		'post' : blog_post,
	}

	return render(request, "dashboard/post-detail.html", context)

# Function to publish a draft post
@login_required(login_url='login')
def publish_post(request, post_id):
	blog_post = get_object_or_404(Post, pk=post_id)
	blog_post.publish()
	messages.success(request, "Success! Blog Post has been published and available to the public.")
	return redirect("dashboard:post_details", post_id=post_id)

@login_required(login_url='login')
def new_blog_post(request):
	if request.method=="POST":
		category = get_object_or_404(Categorie, pk=request.POST['category'])
		post_title = request.POST['post_title']
		post_content = request.POST['post_content']
		featured_img = request.FILES['featured_img']
		author = request.user
		if Post.objects.filter(post_title=post_title).exists():
			messages.error(request, "Error! A blog post with title '{}' already exists. Try another".format(post_title))
			return redirect('blog:new_post')
		else:
			post = Post(category=category, post_title=post_title, post_content=post_content, featured_img=featured_img, author=author)
			post.save()
			messages.success(request, "Success! Blog post details have been saved")
			return redirect('blog:blog_posts')
	else:
		return redirect('blog:new_post')


@login_required(login_url='login')
def edit_post(request, post_id):
	blog_post = get_object_or_404(Post, pk=post_id)
	categories = Categorie.objects.all()

	context = {
		'post' : blog_post,
		'categories' : categories,
	}

	return render(request, "dashboard/edit-post.html", context)

@login_required(login_url='login')
def update_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if request.method=="POST":
		post.category = get_object_or_404(Categorie, pk=request.POST['category'])
		post.post_title = request.POST['post_title']
		post.post_content = request.POST['post_content']
		post.featured_img = request.FILES['featured_img']
		
		post.save()
		messages.success(request, "Success! {} details have been updated.".format(post.post_title))
		return redirect("blog:post_details", post_id=post_id)
	else:
		messages.error(request, "Error! {} details have not been updated.".format(post.post_title))
		return redirect("blog:post_details", post_id=post_id)

# @login_required(login_url='login')
# def allDrafts(request):
# 	posts = Post.objects.filter(published_on__isnull=True).order_by('-created_on')
# 	return render(request, 'blog/posts.html', {'posts':posts})

# @login_required(login_url='login')
# def allPublished(request):
# 	posts = Post.objects.filter(published_on__lte=timezone.now()).order_by('-created_on')
# 	return render(request, 'blog/posts.html', {'posts':posts})

@login_required(login_url='login')
def delete_blog_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.delete()
	return redirect("blog:posts")

# @login_required(login_url='login')
# def posts_comments(request):
# 	comments = Comment.objects.filter(approved_comment=False)
# 	context = {
# 		'comments' : comments,
# 	}
# 	return render(request, 'dashboard/post-comments.html',  context)

# @login_required(login_url='login')
# def approve_comment(request, comment_id):
# 	comment = get_object_or_404(Comment, pk=comment_id)
# 	comment.approved_comment = True
# 	comment.save()
# 	return redirect('dashboard:view-comments')

# @login_required(login_url='login')
# def delete_comment(request, comment_id):
# 	comment = get_object_or_404(Comment, pk=comment_id)
# 	comment.delete()
# 	return redirect('dashboard:view-comments')

# END BLOG FUNCTIONS

