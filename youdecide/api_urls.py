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

from django.urls import include
import home.views as home_views
from polls import urls as polls_urls
from django.urls import path
from account import urls as account_urls
from feed import urls as feed_urls
from trending import urls as trending_urls
from search import urls as search_urls

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
    # urls.py
]

