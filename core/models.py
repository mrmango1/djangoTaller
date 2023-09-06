from django.db import models

# Create your models here.

class SocialNetwork(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    url = models.URLField(verbose_name="Enlace", null=True, blank=True)
    icon = models.CharField(max_length=25, verbose_name="Icono")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Red social"
        verbose_name_plural = "Redes sociales"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
# class Contact(models.Model):
#     name = models.CharField(max_length=50, verbose_name="Nombre")
#     email = models.EmailField(verbose_name="Correo electrónico")
#     subject = models.CharField(max_length=50, verbose_name="Asunto")
#     message = models.TextField(verbose_name="Mensaje")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

#     class Meta:
#         verbose_name = "Contacto"
#         verbose_name_plural = "Contactos"
#         ordering = ['-created_at']

#     def __str__(self):
#         return self.name
    
# class Location(models.Model):
#     name: models.CharField(max_length=50, verbose_name="Nombre")
#     latitude = models.CharField(max_length=50, verbose_name="Latitud")
#     longitude = models.CharField(max_length=50, verbose_name="Longitud")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
        

class Info(models.Model):
    email = models.EmailField(verbose_name="Correo electrónico")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    address = models.CharField(max_length=100, verbose_name="Dirección")
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Ubicación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Información"
        verbose_name_plural = "Información"
        ordering = ['-created_at']

    def __str__(self):
        return self.email
    
