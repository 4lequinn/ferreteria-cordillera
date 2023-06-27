from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="INDEX"),
    path('login/', login, name="LOGIN"),
    path('registro/', registro, name="REGISTRO"),
    path('contacto/', contacto, name="CONTACTO"),
    path('sobre_nosotros/', nosotros, name="SOBRE_NOSOTROS"),
    path('herramientas/', herramientas, name="HERRAMIENTAS"),
    path('accesorios/', accesorios, name="ACCESORIOS"),
    path('productos_construccion/', construccion, name="CONSTRUCCION"),
]