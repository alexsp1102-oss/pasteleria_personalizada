from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cotizacion/', views.landing, name='landing'),
    path('gracias/', views.gracias, name='gracias'),
    path('contacto/', views.contacto, name='contacto'),  # habilitado
]
