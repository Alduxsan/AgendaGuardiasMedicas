from django.contrib import admin
from django.conf.urls import url
#from .views import GuardiasApiView
from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guardias_disponibles', views.GuardiasViewSet, basename='guardias_disponibles')
router.register('modificar_guardia', views.Guardia_modificar, basename='modificar_guardia')
router.register('medico_datos', views.Medico_Datos, basename='medico_datos')


mis_guardias = views.GuardiasViewSet.as_view({
    'get': 'list',
    })

urlpatterns = [
        # path("APIguardias/",views.GuardiasApiView.as_view()),
        url('mis_guardias', mis_guardias, name='mis_guardias'),
        url(r'', include(router.urls))
]