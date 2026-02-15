from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:categoria_slug>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
]