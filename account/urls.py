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
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import (login, logout, logout_then_login, password_change, password_change_done,
                                       password_reset, password_reset_done, password_reset_confirm,
                                       password_reset_complete)
from django.contrib.auth.views import (PasswordResetView, PasswordResetConfirmView,
                                       PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeView,
                                       PasswordChangeDoneView,)  # LogoutView, LoginView,
from rest_framework_simplejwt.views import TokenRefreshView
from account.api import UserCreate, LoginView,  UserListAPIView, ChangePasswordView, UserDetailAPIView
from account import views, api

jwt_urlpattern = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns = [
    # re_path('^logout/$', LogoutView.as_view(), name='logout'),
    # re_path('^logout-then-login/$', logout_then_login, name='logout_then_login'),
    # change password urls
    re_path('^password-change/$', PasswordChangeView.as_view(), name='password_change'),
    re_path('^password-change/done/$', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # restore password urls
    re_path(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password-reset/done/$', PasswordResetDoneView.as_view(),name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    re_path('^register/$', views.register, name='register'),
    # re_path('^$', views.dashboard, name='dashboard'),
    re_path('^edit/$', views.edit, name='edit'),
    # get all users
    re_path('^$', UserListAPIView.as_view(), name='users'),

    # sign up rest api
    path('signup/', UserCreate.as_view(), name="user_create"),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('login/', LoginView.as_view(), name="login"),
    # path('logout/', Logout.as_view(), name='logout'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('', include(jwt_urlpattern))

]

