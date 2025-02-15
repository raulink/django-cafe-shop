from django.contrib import admin

from .models import Product


# Añadir producto para que sea visible en el panel de administración

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'available']
    # Añadir buscadores
    search_fields = ['name', 'price']

admin.site.register(Product, ProductAdmin)