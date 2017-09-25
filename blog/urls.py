from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
	url(r'^$', views.blog_posts, name='blog_posts'),
	url(r'^post-details/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
	url(r'^subscribe/$', views.subscribe, name='subscribe'),
]