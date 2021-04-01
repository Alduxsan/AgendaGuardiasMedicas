
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'Cuentas'

urlpatterns= [
    url('login', views.ingresar, name ='login'),
    url('logout', views.salir, name ='logout'),
    
]

