# 应用url
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'detail/(\d+)', views.detail),
    url(r'vote/(\d+)$', views.vote),
]