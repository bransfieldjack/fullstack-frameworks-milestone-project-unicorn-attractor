from django.conf.urls import url
from .views import index, login


urlpatterns = [
    url(r'^login/$', login, name='login'),
    ]