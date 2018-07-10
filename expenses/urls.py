from .views import ProviderViewFilterSet

from rest_framework import routers
from django.conf.urls import url
from django.urls import include

router = routers.DefaultRouter()

router.register('proveedores', ProviderViewFilterSet, 'proveedores')

app_name='expenses'

urlpatterns = [
    url('^', include(router.urls)),
]
