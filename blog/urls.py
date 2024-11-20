from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.blog_posts, name='blog_posts'),
	path('post-details/<int:pk>/', views.post_detail, name='post_detail'),
	path('subscribe/', views.subscribe, name='subscribe'),

	# Admin
	path('categories', views.blog_categories, name='blog_categories'),
	path('register-category', views.register_category, name='register_category'),
	path('category/<int:category_id>/', views.blog_category_details, name='category_details'),
	path('edit-category/<int:category_id>/', views.edit_blog_category, name='edit_category'),
	path('update-category/<int:category_id>/', views.update_blog_category, name='update_blog_category'),
	path('delete-category/<int:category_id>/', views.delete_blog_category, name='delete_category'),
	path('new-post/', views.new_post, name='new_post'),
	path('save-post/', views.new_blog_post, name='save_post'),
	path('blog/', views.view_posts, name='posts'),
	path('post-detail/<int:post_id>/', views.post_details, name='post_details'),
	path('publish-post/<int:post_id>/', views.publish_post, name='publish_post'),
	path('edit-post/<int:post_id>/', views.edit_post, name='edit_post'),
	path('update-post/<int:post_id>/', views.update_post, name='update_post'),
	path('delete-post/<int:post_id>/', views.delete_blog_post, name='delete_post'),
]