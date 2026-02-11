from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ("nombre",)
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    corta_descripcion = models.TextField(max_length=300, blank=True)
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos/", blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default="", blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("nombre",)
        verbose_name = "producto"
        verbose_name_plural = "productos"
        
    def __str__(self):
        return self.nombre