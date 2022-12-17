from django.contrib import admin
from .models import Platos
# Register your models here.
@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
  list_display = ('nombre_plato','precio','procedencia')
  list_filter = ('nombre_plato',)
  search_fields = ('nombre_plato',)
  fields = ('nombre_plato','precio','procedencia')
