from django.conf.urls import url

from . import views

app_name = 'store'

urlpatterns = [
	url(r'^$', views.all_products, name='products'),
	url(r'^product/(?P<pk>\d+)/detail/$', views.product_detail, name='product_detail'),
]