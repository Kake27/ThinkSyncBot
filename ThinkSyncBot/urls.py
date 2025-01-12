from django.urls import path
from . import views
from .views import get_name

urlpatterns = [
    path("", views.base),
    path("get/", get_name, name="get_name")
]