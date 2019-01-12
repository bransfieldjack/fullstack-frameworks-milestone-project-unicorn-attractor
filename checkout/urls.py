from django.conf.urls import url
from checkout.views import view_cart, add_to_cart,checkout


urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^$', view_cart, name='view_cart'),
]
