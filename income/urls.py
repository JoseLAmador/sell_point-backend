from .views import IncomeViewSet, UserViewSet

from rest_framework import routers
from django.conf.urls import url
from django.urls import include

router = routers.DefaultRouter()

router.register('incomes', IncomeViewSet)
router.register('users', UserViewSet)

app_name='income'

urlpatterns = [
    url('^', include(router.urls)),
]
