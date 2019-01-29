"""chenglei_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet, CustomAuthToken

router = DefaultRouter()

#用户接口
router.register(r'user', UserViewSet, base_name="user")

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api-token-auth/', CustomAuthToken.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'docs/', include_docs_urls(title='成磊科技')),
]