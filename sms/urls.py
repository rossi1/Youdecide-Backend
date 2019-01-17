from django.urls import path, include, re_path
# from .views import polls_list, polls_detail
from polls import api
from django.urls import path
from .api import UserCreateSMS


urlpatterns = [

    path("text-msg/", UserCreateSMS.as_view(), name="create_sms"),

]