from django.contrib import admin
from .models import ServiceCategory, ServiceProvider

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'phone', 'verified')
    list_filter = ('category', 'verified')
    search_fields = ('name', 'phone')