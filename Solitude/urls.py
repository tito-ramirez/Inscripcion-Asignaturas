"""Solitude URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from SolitudeS2.views import vista1clase
from SolitudeS2.views import logout_view
from SolitudeS2.views import Solicitud_por_tope
from SolitudeS2.views import Solicitud_sin_prerequisito
from SolitudeS2.views import Ver_solicitudes
from SolitudeS2.views import crear_Solicitud_por_tope
from SolitudeS2.views import crear_Solicitud_sin_requisito 
from SolitudeS2.views import visualizar_solicitudes_e
from SolitudeS2.views import modificarestado_portope
from SolitudeS2.views import modificarestado_por_tope2
from SolitudeS2.views import modificarestado_sinreq
from SolitudeS2.views import modificarestado_sinreq2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='index.html')),
    path('accounts/profile/', vista1clase.as_view()),
    path('Solicitud_por_tope', Solicitud_por_tope.as_view()),
    path('Solicitud_sin_prerequisito', Solicitud_sin_prerequisito.as_view()),
    path('Ver_solicitudes', Ver_solicitudes.as_view()),
    path('crearsolitope', crear_Solicitud_por_tope.as_view()),
    path('visualizar_solicitudes_e', visualizar_solicitudes_e.as_view()),
    path('crearsolisrequisito', crear_Solicitud_sin_requisito.as_view()),
    path('modificarestado_por_tope2', modificarestado_por_tope2.as_view()),
    path('modificarestado_portope', modificarestado_portope.as_view()),
    path('modificarestado_sinreq2', modificarestado_sinreq2.as_view()),
    path('modificarestado_sinreq', modificarestado_sinreq.as_view()),
    path('accounts/profile/logout_view',logout_view, name='accounts/profile/logout_view'),
]