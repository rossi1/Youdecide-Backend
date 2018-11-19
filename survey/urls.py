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
from survey.api import CategoryAPIListView, CategoryAPIDetailView, SurveyQuestionAPIListView, SurveyQuestionAPIDetailView


urlpatterns = [
    re_path('category/(?P<pk>[0-9]+)/$', CategoryAPIDetailView.as_view(), name='category'),
    re_path('categories/$', CategoryAPIListView.as_view(), name='categories'),
    re_path('question/(?P<pk>[0-9]+)/$', SurveyQuestionAPIDetailView.as_view(), name='survey_question'),
    re_path('questions/$', SurveyQuestionAPIListView.as_view(), name='survey_questions'),
]
