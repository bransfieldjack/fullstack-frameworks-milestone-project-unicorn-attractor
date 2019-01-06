from django.conf.urls import url
from checkout.views import cart


urlpatterns = [
    url(r'^cart$', cart, name='cart'),
]
