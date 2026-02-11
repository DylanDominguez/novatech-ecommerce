from django.contrib import admin
from .models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    prepopulated_fields = {"slug": ("nombre",)}
    list_per_page = 20
admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "creado_en", "actualizado_en"]
    prepopulated_fields = {"slug": ("nombre",)}
    list_per_page = 20
admin.site.register(Producto, ProductoAdmin)