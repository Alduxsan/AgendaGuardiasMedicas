from django.urls import path, re_path

from . import views

app_name = "login_app"

urlpatterns = [
    path("", views.indexView.as_view()),
    
]