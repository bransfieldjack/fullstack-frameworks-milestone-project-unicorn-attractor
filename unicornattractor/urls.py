"""unicornattractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from tickets import urls as urls_tickets
from accounts.views import index, login, register, logout, user_profile
from tickets.views import tickets, bugs, features, edit_bug, edit_feature, add_feature, add_bug, bug_detail, features_detail
from accounts import urls as accounts_urls


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
]
