from django.conf.urls import url

from . import views

app_name = 'dashboard'

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	# Accounts
	# url(r'^new-account/$', views.new_account, name='new_account'),
	# url(r'^create-account/$', views.create_account, name='create_account'),

	# Blog

	# Store
]