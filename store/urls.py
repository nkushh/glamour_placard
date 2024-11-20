from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
	path('', views.all_products, name='products'),
	path('product/<int:pk>/detail/', views.product_detail, name='product_detail'),

	# Admin side
	path('new-category/', views.new_category, name='new_category'),
	path('item-categories/', views.item_categories, name='item_categories'),
	path('delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
	path('sub-categories/<int:category_id>/', views.all_subcategories, name='sub_categories'),
	path('add-subcategory/', views.new_subcategory, name='new_subcategory'),
	path('items/', views.all_items, name='all_items'),
	path('new-item/', views.new_item, name='new_item'),
	path('add-item/', views.add_item, name='add_item'),
]