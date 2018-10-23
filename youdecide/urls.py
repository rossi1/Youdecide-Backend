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
from django.urls import path, re_path
from django.views.generic import TemplateView
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('polls', include(polls_urls)),
    path('api/', include(api_urls)),
    # urls.py
    # path(r"^wizard/$", "my_form_wizard_view", name="my_form_wizard_view"),
    re_path('.*', TemplateView.as_view(template_name='youdecide_frontend/index.html')),

    # account urls
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),
    # login / logout urls
    path('^login/$', 'django.contrib.auth.views.login', name='login'),
    path('^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    path('^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),

    # change password urls
    path('^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    path('^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),

    # restore password urls
    path(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    path(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done',name='password_reset_done'),
    path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
         'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    path(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    path('^$', views.dashboard, name='dashboard'),
]
