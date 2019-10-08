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

from django.urls import include, path
from django.conf.urls import url
import home.views as home_views
from polls import urls as polls_urls
from django.urls import path
from account import urls as account_urls
from feed import urls as feed_urls
from trending import urls as trending_urls
from search import urls as search_urls
from userprofile import urls as userprofile_urls
from notification import urls as notification_urls
from sms import urls as sms_urls
from social import urls as social_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Youdecide",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="youdecide"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_patterns = [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]

urlpatterns = [
    path('', home_views.home, name='home'),
    path('polls/', include(polls_urls)),
    # path('api/', include(api_urls)),
    # path('survey/', include(survey_urls)),

    # account urls
    path('users/', include(account_urls)),
    path('feeds/', include(feed_urls)),
    path('trending/', include(trending_urls)),
    path('search/', include(search_urls)),
    path('sms/', include(sms_urls)),
    path('userprofile/', include(userprofile_urls)),
    path('notification/', include(notification_urls)),
    path('social/', include(social_urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
    # urls.py
]

