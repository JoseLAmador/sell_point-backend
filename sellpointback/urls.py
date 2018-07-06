"""sellpointback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from income import urls as incomesUrls

from django.conf.urls import url
from accounts import urls as authUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(r'users/', include('accounts.urls')),


    path('api/auth/', include(authUrls, namespace='auth-urls')),
    path('api/incomes/', include(incomesUrls, namespace="incomes-urls")),

    url(r'^api-auth/', include('rest_framework.urls')),
]
