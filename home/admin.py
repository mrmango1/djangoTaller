from django.contrib import admin
from .models import Carousel
# Register your models here.

class CarouselAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Carousel, CarouselAdmin)

