"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from hello_world.core import views as core_views

urlpatterns = [
    path("", core_views.index),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('services/', core_views.services, name="services"),
    path('store/', core_views.store, name="store"),
    path('contact/', core_views.contact, name="contact"),
    path('blog/', core_views.blog, name="blog"),
    path('sample/', core_views.sample, name="sample"),
    #path('', Home.as_view(), name='home'),
    #path('blog/', include('blog.urls')),
]
