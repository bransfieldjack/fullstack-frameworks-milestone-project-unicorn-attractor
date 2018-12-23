from django.conf.urls import url
from .views import tickets, add_bug, add_feature


urlpatterns = [
    url(r'^tickets/$', tickets, name='tickets'),
    url(r'^add_bug/$', add_bug, name='add_bug'),
    url(r'^add_feature/$', add_feature, name='add_feature'),
    ]