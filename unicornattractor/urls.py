from django.conf.urls import url, include
from django.contrib import admin
from tickets import urls as urls_tickets
from accounts.views import index, login, register, logout, user_profile
from tickets.views import tickets, bugs, features, edit_bug, edit_feature, add_feature, add_bug, bug_detail, features_detail, bug_upvote, bug_downvote, feature_upvote, feature_downvote
from accounts import urls as accounts_urls
from checkout.views import view_cart, add_to_cart, checkout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),    # If there is no name after slash, display index. 
    url(r'^accounts/', include(accounts_urls)),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^accounts/user_profile/$', user_profile, name='user_profile'),
    url(r'^tickets/', tickets, name='tickets'),
    url(r'^bugs/', bugs, name='bugs'),
    url(r'^features/', features, name='features'),
    url(r'(?P<pk>\d+)/edit_bug/$', edit_bug, name='edit_bug'),
    url(r'^add_bug/$', add_bug, name='add_bug'),
    url(r'^add_feature/', add_feature, name='add_feature'),
    url(r'(?P<pk>\d+)/edit_feature/$', edit_feature, name='edit_feature'),
    url(r'(?P<pk>\d+)/bug_detail/$', bug_detail, name='bug_detail'),
    url(r'(?P<pk>\d+)/features_detail/$', features_detail, name='features_detail'),
    url(r'(?P<pk>\d+)/bug_upvote/$', bug_upvote, name='bug_upvote'),
    url(r'(?P<pk>\d+)/bug_downvote/$', bug_downvote, name='bug_downvote'),
    url(r'(?P<pk>\d+)/feature_upvote/$', feature_upvote, name='feature_upvote'),
    url(r'(?P<pk>\d+)/feature_downvote/$', feature_downvote, name='feature_downvote'),
    url(r'^view_cart/$', view_cart, name='view_cart'),
    url(r'(?P<pk>\d+)/add_to_cart/$', add_to_cart, name='add_to_cart'),
    url(r'^checkout/$', checkout, name='checkout'),
]
