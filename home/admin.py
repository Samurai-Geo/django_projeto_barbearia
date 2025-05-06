from django.contrib import admin
from home import models

@admin.register(models.Barbeiro)
class BarbeiroAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'apelido', 'nome', 'sobrenome', 'telefone',
    )
    ordering = 'id',
    list_filter = 'data_criada',
    search_fields = 'id', 'apelido', 'nome', 'sobrenome', 'telefone','email',
    list_per_page = 10
    list_max_show_all = 200
    # list_editable = 'show',
    list_display_links = 'id', 'apelido', 'nome', 'sobrenome',
