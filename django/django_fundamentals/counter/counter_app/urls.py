from django.urls import path
from . import views

urlpatterns = [
    path("",views.root),
    path("distroy_session/",views.distroy),
]