from django.conf.urls import url, include
from .views import tickets, edit_bug, edit_feature, add_feature, add_bug, bug_detail, features_detail, bug_upvote, bug_downvote, feature_upvote, feature_downvote
from checkout import urls as urls_checkout


urlpatterns = [
    url(r'^tickets/$', tickets, name='tickets'),
    url(r'(?P<pk>\d+)/edit_bug/$', edit_bug, name='edit_bug'),
    url(r'(?P<pk>\d+)/edit_feature/$', edit_feature, name='edit_feature'),
    url(r'^add_bug/$', add_bug, name='add_bug'),
    url(r'^add_feature/$', add_feature, name='add_feature'),
    url(r'(?P<pk>\d+)/bug_detail/$', bug_detail, name='bug_detail'),
    url(r'(?P<pk>\d+)/features_detail/$', features_detail, name='features_detail'),
    url(r'(?P<pk>\d+)/bug_upvote/$', bug_upvote, name='bug_upvote'),
    url(r'(?P<pk>\d+)/bug_downvote/$', bug_downvote, name='bug_downvote'),
    url(r'(?P<pk>\d+)/feature_upvote/$', feature_upvote, name='feature_upvote'),
    url(r'(?P<pk>\d+)/feature_downvote/$', feature_downvote, name='feature_downvote'),
    url(r'^cart/', include(urls_checkout)),
    ]
    
    