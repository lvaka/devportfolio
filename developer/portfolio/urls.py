from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)