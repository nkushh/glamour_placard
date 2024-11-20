"""glamour_placard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url('^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', auth_views.login, {'template_name': 'authentication/login.html'}, name='login'),
    # path('logout/', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    path('admin/', admin.site.urls),
    path('', include('about.urls', namespace='about')),
    path('authentication/', include('authentication.urls', namespace='authentication')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('store/', include('store.urls', namespace='store')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
