from django.urls import path
from .import views    #importamos las vistas de la app

urlpatterns = [
    path('',views.home,name='home')  #definir la ruta principal de la app
]

