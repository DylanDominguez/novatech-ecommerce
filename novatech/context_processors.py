from .models import Categoria

def categorias(request):
    categorias = Categoria.objects.order_by("-nombre")
    return dict(categorias = categorias)