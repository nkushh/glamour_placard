from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
	url(r'^$', views.blog_posts, name='blog_posts'),
	url(r'^blog/$', views.view_posts, name='posts'),
	url(r'^categories', views.blog_categories, name='blog_categories'),
	url(r'^register-category', views.register_category, name='register_category'),
	url(r'^category/(?P<category_id>\d+)/$', views.blog_category_details, name='category_details'),
	url(r'^edit-category/(?P<category_id>\d+)/$', views.edit_blog_category, name='edit_category'),
	url(r'^update-category/(?P<category_id>\d+)/$', views.update_blog_category, name='update_blog_category'),
	url(r'^delete-category/(?P<category_id>\d+)/$', views.delete_blog_category, name='delete_category'),
	url(r'^new-post/$', views.new_post, name='new_post'),
	url(r'^save-post/$', views.new_blog_post, name='save_post'),
	url(r'^post-details/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
	url(r'^subscribe/$', views.subscribe, name='subscribe'),
]