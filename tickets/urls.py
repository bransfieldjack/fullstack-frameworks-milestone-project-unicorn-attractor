from django.conf.urls import url
from .views import tickets, add_bug, add_feature, bug_detail, features_detail


urlpatterns = [
    url(r'^tickets/$', tickets, name='tickets'),
    url(r'^add_bug/$', add_bug, name='add_bug'),
    url(r'^add_feature/$', add_feature, name='add_feature'),
    url(r'(?P<pk>\d+)/bug_detail/$', bug_detail, name='bug_detail'),
    url(r'(?P<pk>\d+)/features_detail/$', features_detail, name='features_detail'),
    ]