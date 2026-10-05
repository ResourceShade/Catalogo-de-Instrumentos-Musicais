from django.contrib import admin
from .models import Instrumento


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'estoque', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nome', 'categoria')
