from django.contrib import admin
from django.conf.urls import url
from .views import GuardiasApiView
from api import views
from django.urls import include, path



urlpatterns = [
        path("APIguardias/",views.GuardiasApiView.as_view()),
]