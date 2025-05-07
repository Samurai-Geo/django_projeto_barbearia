from django.contrib import admin
from home import models

@admin.register(models.Barbeiro)
class BarbeiroAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'apelido', 'nome', 'sobrenome', 'telefone', 'chave_pix', 'show',
    )
    ordering = 'id',
    list_filter = 'data_criada',
    search_fields = 'id', 'apelido', 'nome', 'sobrenome', 'telefone','email',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'show',
    list_display_links = 'id', 'apelido', 'nome', 'sobrenome',

@admin.register(models.CategoriaUser)
class CategoriaBarberAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',

@admin.register(models.Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'identificacao', 'valor', 'categoria_servico', 'show',
    )
    ordering = 'id',
    list_filter = 'data_criada',
    search_fields = 'id', 'identificacao',
    list_per_page = 20
    list_max_show_all = 200
    list_editable = 'valor', 'categoria_servico', 'show'
    list_display_links = 'id', 'identificacao'

@admin.register(models.CategoriaServico)
class CategoriaServicoAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
