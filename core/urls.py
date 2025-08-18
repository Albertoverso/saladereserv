from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('salas/', views.salas, name='salas'),
    path('salas/nova/', views.sala_nova, name='sala_nova'),
    path('salas/<int:id>/editar/', views.sala_editar, name='sala_editar'),
    path('salas/<int:id>/excluir/', views.sala_excluir, name='sala_excluir'),
    path('reservas/', views.reservas, name='reservas'),
    path('reservas/nova/', views.reserva_nova, name='reserva_nova'),
    path('reservas/<int:id>/cancelar/', views.reserva_cancelar, name='reserva_cancelar'),
]
