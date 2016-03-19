from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.createWarden, name='chiefwarden-home'),
    url(r'^add-branch/$',views.addbranch, name='chiefwarden-add-branch'),
]