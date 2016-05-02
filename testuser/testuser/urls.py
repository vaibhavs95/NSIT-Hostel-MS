"""testuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
handler400 = 'newapp.views.bad_request'
handler403 = 'newapp.views.permission_denied'
handler404 = 'newapp.views.page_not_found'
handler500 = 'newapp.views.server_error'
urlpatterns = [
    # url(r'^newapp/',include('newapp.urls')),
    url(r'^chiefwarden/',include('chief.urls')),
    url(r'^warden/',include('warden.urls')),
    url(r'^student/',include('student.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('newapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
