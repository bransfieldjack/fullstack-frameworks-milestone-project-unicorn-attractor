from django.conf.urls import url, include
from .views import get_data, stats, ChartData


urlpatterns = [
    url(r'^get_data/', get_data, name='get_data'),
    url(r'^stats/', stats, name='stats'),
    url(r'^ChartData/$', ChartData.as_view(), name='ChartData'),
    ]
    
    