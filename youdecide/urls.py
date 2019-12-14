# demo_project/urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from youdecide import api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler500 = 'youdecide.account.api.server_error'
handler404 = 'youdecide.account.api.not_found_request'