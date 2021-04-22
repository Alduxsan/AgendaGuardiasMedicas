from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from api import views
from api.scheduler import start_jobs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', include("Aplicaciones.login.urls")),
    #re_path(r'^', include("Aplicaciones.Cuentas.urls")),
    re_path(r'^', include("Aplicaciones.GuardiasAsignadas.urls")),
    re_path(r'^', include("Aplicaciones.GuardiasDisponibles.urls")),
    re_path(r'^', include("Aplicaciones.DevolucionGuardias.urls")),
    path('accounts/', include('django.contrib.auth.urls')),

    path('',include('api.urls'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

start_jobs()