from django.shortcuts import render
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