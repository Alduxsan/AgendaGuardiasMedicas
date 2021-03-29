from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from api import views


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', include("Aplicaciones.login.urls")),
    re_path(r'^', include("Aplicaciones.Cuentas.urls")),
    re_path(r'^', include("Aplicaciones.GuardiasAsignadas.urls")),
    re_path(r'^', include("Aplicaciones.GuardiasDisponibles.urls")),
    re_path(r'^', include("Aplicaciones.DevolucionGuardias.urls")),
    path('accounts/', include('django.contrib.auth.urls')),

    path('',include('api.urls'))
]

urlpatterns += staticfiles_urlpatterns()


