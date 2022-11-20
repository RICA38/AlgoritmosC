from . import views
from django.urls import path

urlpatterns = [
    path('Knn/', views.muestra_datos, name='Knn'),
]
