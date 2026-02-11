from django.shortcuts import render
from .models import Categoria, Producto

def index(request):
    productos = Producto.objects.order_by("-categoria")
    context = {
        "productos": productos
    }
    return render(request, 'novatech/index.html', context)