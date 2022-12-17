from django.contrib import admin

from .models import Clientes
# Register your models here.
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
  list_display = ('nombre_cliente','apellido','dni')
  list_filter = ('nombre_cliente',)
  search_fields = ('nombre_cliente',)
  fields = ('nombre_cliente','apellido','dni')
