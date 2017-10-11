from django.conf.urls import url

from . import views

app_name = 'store'

urlpatterns = [
	url(r'^$', views.all_products, name='products'),
	url(r'^product/(?P<pk>\d+)/detail/$', views.product_detail, name='product_detail'),

	# Admin side
	url(r'^new-category/$', views.new_category, name='new_category'),
	url(r'^item-categories/$', views.item_categories, name='item_categories'),
	url(r'^delete-category/(?P<category_id>\d+)/$', views.delete_category, name='delete_category'),
	url(r'^sub-categories/(?P<category_id>\d+)/$', views.all_subcategories, name='sub_categories'),
	url(r'^items/$', views.all_items, name='all_items'),
]