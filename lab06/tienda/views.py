from django.shortcuts import render
from .models import Producto, Categoria

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()  
    context = {'product_list': product_list, 'categorias': categorias}
    return render(request, 'index.html', context)

def producto(request):
    return render(request, 'producto.html')

def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    context = {'categoria': categoria, 'productos': productos}
    return render(request, 'productos/productos_por_categoria.html', context)






