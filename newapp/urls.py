from django.urls import path
from . import views

# Aqui Cree los url para cada una de las vistas que tiene mi Aplicacion para Agregar miembros trabajadores.

urlpatterns = [
    path('Index/', views.index,name='index'),
    path('add/', views.add,name="add" ),
    path("addrec/", views.addrec,name="addrec"),
    path('eliminar/<int:id>/', views.eliminar,name="eliminar"),
    path('actualizar/<int:id>/',views.update,name="actualizar"),
    path('actualizar/uprec/<int:id>/',views.uprec,name="uprec"),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]