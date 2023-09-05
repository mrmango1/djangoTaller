from django.db import models

# Create your models here.

class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel', verbose_name='Imagen')
    title = models.CharField(max_length=100, verbose_name='Título')
    subtitle = models.CharField(max_length=100, verbose_name='Subtítulo')
    description = models.TextField(verbose_name='Descripción')
    link = models.URLField(max_length=200, verbose_name='Enlace')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'carusel'
        verbose_name_plural = 'caruseles'
        ordering = ['-created_at']

    def __str__(self):
        return self.title