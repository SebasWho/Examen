"""parcial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from parcial import views as general
from users import views as users
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls, name="administracion"),
    path('inicio/', general.homepage, name="homepage"),
    path('', users.logon, name= "logon"),
    path('Clinica/', users.CITAS, name= "citas"),
    path('REGISTRO/', users.registro, name= "registro"),
    path('busqueda/', users.buscar, name= "busqueda"),
    path('pacientes/', users.pacientes, name= "pacientes"),
    path('logout/', users.logout_view, name= "logout"),
    path('boletos/', users.VUELOS, name= "boletos"),
    path('bitacora/', users.factura, name= "factura"),
    path('factura/', users.bitacora, name= "bitacora"),
    path('eliminar/', users.bitacora, name= "eliminar"),
    path('borrar/', users.borrar, name= "borrar"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)