from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from knox import views as knox_views

from . import views
from.views import LoginAPI

router = DefaultRouter()
router.register('guardias_disponibles', views.GuardiasViewSet, basename='guardias_disponibles')
router.register('mis_guardias', views.MisGuardias, basename='mis_guardias')
router.register('modificar_guardia', views.Guardia_modificar, basename='modificar_guardia')
router.register('medico_datos', views.Medico_Datos, basename='medico_datos')
router.register('MartyMcFly', views.MartyMcFly, basename='MartyMcFly')

urlpatterns = [
        # path("APIguardias/",views.GuardiasApiView.as_view()),
        url(r'', include(router.urls)),
        path('api/api_login/', LoginAPI.as_view(), name='api_login'),
        path('api/api_logout/', knox_views.LogoutView.as_view(), name='api_logout'),
        path('api/api_logoutall/', knox_views.LogoutAllView.as_view(), name='api_logout_all'),
]