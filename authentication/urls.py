from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'authentication'

urlpatterns = [
	url(r'^create-account/$', views.create_account, name='create_account'),
	url(r'^accounts/$', views.all_accounts, name='accounts'),
	url(r'^deactivate-account/(?P<account>\d+)/$', views.deactivate_account, name='deactivate-account'),
	url(r'^activate-account/(?P<account>\d+)/$', views.activate_account, name='activate-account'),
	url(r'^delete-account/(?P<account>\d+)/$', views.delete_account, name='delete-account'),
]