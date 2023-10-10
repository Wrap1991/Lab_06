from django.urls import path

from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    path('categorias/', views.categorias, name='categorias'),  
    path('categorias/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),  # Nueva URL para listar productos por categoría
]

