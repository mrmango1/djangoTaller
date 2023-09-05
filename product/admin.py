from django.contrib import admin
from .models import Category, ProductImage, Color, Size, Clothes

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(ProductImage, ProductImageAdmin)

class ColorAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Color, ColorAdmin)

class SizeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Size, SizeAdmin)

class ClothesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Clothes, ClothesAdmin)