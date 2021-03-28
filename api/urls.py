from django.contrib import admin
from django.conf.urls import url
from .views import GuardiasApiView
from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guardias-viewset', views.GuardiasViewSet, basename='guardias-viewset')

urlpatterns = [
        path("APIguardias/",views.GuardiasApiView.as_view()),
        url(r'', include(router.urls))
]