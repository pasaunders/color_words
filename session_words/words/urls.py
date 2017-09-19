from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.rendering),
    url(r'^add', views.add),
    url(r'^clear', views.clear)
]