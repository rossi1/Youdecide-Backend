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


from django.urls import path, include, re_path
from account import views
from django.contrib.auth.views import (login, logout, logout_then_login, password_change, password_change_done,
                                        password_reset, password_reset_done, password_reset_confirm, password_reset_complete)

urlpatterns = [
    re_path('^login/$', login, name='login'),
    re_path('^logout/$', logout, name='logout'),
    re_path('^logout-then-login/$', logout_then_login, name='logout_then_login'),

    # change password urls
    re_path('^password-change/$', password_change, name='password_change'),
    re_path('^password-change/done/$', password_change_done, name='password_change_done'),

    # restore password urls
    re_path(r'^password-reset/$', password_reset, name='password_reset'),
    re_path(r'^password-reset/done/$', password_reset_done,name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
         password_reset_confirm, name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),


    re_path('^register/$', views.register, name='register'),
    re_path('^$', views.dashboard, name='dashboard'),
    re_path('^edit/$', views.edit, name='edit'),
]