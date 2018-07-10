from .views import IncomeViewSet, UserViewSet, ClienteViewSet, ClienteViewFilterSet

from rest_framework import routers
from django.conf.urls import url
from django.urls import include

router = routers.DefaultRouter()

router.register('incomes', IncomeViewSet)
router.register('users', UserViewSet)
#router.register('clientes', ClienteViewSet)
router.register('clientes', ClienteViewFilterSet, 'clientes')

app_name='income'

urlpatterns = [
    url('^', include(router.urls)),
]
