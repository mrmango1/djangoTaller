from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Categoría")
    description = models.TextField(verbose_name="Descripción")
    img = models.ImageField(upload_to="categories", null=True, blank=True, verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to="products", null=True, blank=True, verbose_name="Imagen Secundaria")
    description = models.CharField(max_length=200, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imágenes"
        ordering = ["-created_at"]

class Color(models.Model):
    name = models.CharField(max_length=200, verbose_name="Color")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "color"
        verbose_name_plural = "colores"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

class Size(models.Model):
    size = models.CharField(max_length=200, verbose_name="Talla")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "talla"
        verbose_name_plural = "tallas"
        ordering = ["-created_at"]

    def __str__(self):
        return self.size
    
class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name="Marca")
    img = models.ImageField(upload_to="brands", null=True, blank=True, verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    spects = models.TextField(verbose_name="Especificaciones")
    brand = models.CharField(max_length=200, verbose_name="Marca")
    category = models.ManyToManyField("Category", verbose_name="Categorías")
    price = models.FloatField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    rating = models.FloatField(verbose_name="Calificación")
    mainImage = models.ImageField(upload_to="products", null=True, blank=True, verbose_name="Imagen Principal")
    images = models.ManyToManyField("ProductImage", verbose_name="Imágenes")
    created_by = models.ForeignKey(User, verbose_name="Creado por", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

class Clothes(Product):
    size = models.ManyToManyField("Size", verbose_name="Tallas")
    color = models.ManyToManyField("Color", verbose_name="Colores")

    class Meta:
        verbose_name = "ropa"
        verbose_name_plural = "ropas"
        ordering = ["-created_at"]

