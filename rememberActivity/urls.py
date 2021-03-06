"""rememberActivity URL Configuration

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
from django.urls import path, include
import xadmin

from rememberActivity.settings import MEDIA_ROOT
from django.views.static import serve
from images.views import ImagesViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'images', ImagesViewSet, base_name="images")

urlpatterns = [
    path('admin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),
    url(r'^', include(router.urls)),
    # 商品列表页
    url(r'docs/', include_docs_urls(title="暮雪生鲜")),
]
