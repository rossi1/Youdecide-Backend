"""youdecide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import home.views as home_views
from polls import urls as polls_urls
from api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', home_views.home, name='home'),
    path('', include(polls_urls)),
    path('api/', include(api_urls)),
    # urls.py
    path(r"^wizard/$", "my_form_wizard_view", name="my_form_wizard_view"),
]
