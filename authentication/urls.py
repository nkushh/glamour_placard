from django.urls import path
from django.contrib import admin

from . import views

app_name = 'authentication'

urlpatterns = [
	path('create-account/', views.create_account, name='create_account'),
	path('accounts/', views.all_accounts, name='accounts'),
	path('deactivate-account/<int:account>/', views.deactivate_account, name='deactivate-account'),
	path('activate-account/<int:account>/', views.activate_account, name='activate-account'),
	path('delete-account/<int:account>/', views.delete_account, name='delete-account'),
]