"""sandbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from caesar.views import home

urlpatterns = [

    path('', include('django.contrib.auth.urls')),

    path('i18n/', include('django.conf.urls.i18n')),

    path('admin/', admin.site.urls),

    path('', home.home_page, name='home'),

    path('products/', include(('caesar.urls', 'caesar'), namespace='products')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
