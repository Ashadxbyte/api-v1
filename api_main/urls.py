from django.urls import path
from api_main import views

urlpatterns = [
    path('', views.index, name='index'),
]