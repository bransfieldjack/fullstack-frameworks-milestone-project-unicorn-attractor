from django.conf.urls import url, include
from .views import index, login
from accounts.views import index, login, register, logout, user_profile
import url_reset


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^user_profile/$', user_profile, name='user_profile'),
    url(r'^password-reset/$', include(url_reset)),
    ]