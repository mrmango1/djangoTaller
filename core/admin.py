from django.contrib import admin
from .models import SocialNetwork, Info
# Register your models here.

class SocialNetworkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(SocialNetwork, SocialNetworkAdmin)

class InfoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Info, InfoAdmin)