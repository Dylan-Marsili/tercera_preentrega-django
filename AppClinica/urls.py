"""
URL configuration for tercera_preentrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import inicio, empleados,empleados_habu, clientes, clientes_habu, response, citas, citas_habu

urlpatterns = [
    path('', inicio, name='inicio'),
    path('empleados/', empleados, name='empleados'),
    path('empleados_habu/', empleados_habu, name='empleados_habu'),
    path('clientes/', clientes, name='clientes'),
    path('clientes_habu/', clientes_habu, name='clientes_habu'),
    path('citas/', citas, name='citas'),
    path('citas_habu/', citas_habu, name='citas_habu'),
    path('response/', response, name='response'),
]
