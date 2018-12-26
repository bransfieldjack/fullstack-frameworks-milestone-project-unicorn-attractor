from django.conf.urls import url
from .views import tickets, edit_bug, edit_feature, add_feature, add_bug, bug_detail, features_detail


urlpatterns = [
    url(r'^tickets/$', tickets, name='tickets'),
    url(r'(?P<pk>\d+)/edit_bug/$', edit_bug, name='edit_bug'),
    url(r'(?P<pk>\d+)/edit_feature/$', edit_feature, name='edit_feature'),
    url(r'^add_bug/$', add_bug, name='add_bug'),
    url(r'^add_feature/$', add_feature, name='add_feature'),
    url(r'(?P<pk>\d+)/bug_detail/$', bug_detail, name='bug_detail'),
    url(r'(?P<pk>\d+)/features_detail/$', features_detail, name='features_detail'),
    ]