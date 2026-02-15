from django.shortcuts import get_object_or_404, redirect, render
from .models import Categoria, Producto
from django.core.paginator import Paginator

def index(request):
    productos = Producto.objects.order_by("-categoria")
    paginator = Paginator(productos, 8)  # Mostrar 10 productos por página
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)
    
    context = {
        "productos": obj_pagina,
    }
    return render(request, 'novatech/index.html', context)

def productos_por_categoria(request, categoria_slug = None):
    categoria_producto = None
    productos = None
    
    if categoria_slug != None:
        categoria_producto = get_object_or_404(Categoria, slug = categoria_slug)
        productos = Producto.objects.filter(categoria=categoria_producto)
    
    paginator = Paginator(productos, 8)  # Mostrar 10 productos por página
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)
    
    context = {
        "productos": obj_pagina,
    }
    
    return render(request, 'novatech/index.html', context)

def producto_detalle(request, pk):
    producto_detalle = get_object_or_404(Producto, pk = pk)
    
    context = {
        "producto_detalle": producto_detalle,
    }
    
    return render(request, 'novatech/producto_detalle.html', context)
