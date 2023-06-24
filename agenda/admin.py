from django.contrib import admin
from agenda.models import Agenda, Local, Convidado, Categoria, Produto
from django.contrib.admin.filters import SimpleListFilter   # Para fazer filtros personalizados

# Register your models here.
class ConvidadosInline(admin.TabularInline):
    model = Agenda.convidados.through


class ConvidadoAdmin(admin.ModelAdmin):
    inlines = [
        ConvidadosInline,
    ]


class AgendaAdmin(admin.ModelAdmin):
    inlines = [
        ConvidadosInline,
    ]
    exclude = ['convidados']


admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Local)
admin.site.register(Convidado, ConvidadoAdmin)

# ----------------- Parte de teste -------------
admin.site.register(Categoria)


class CategoriaAdmin(admin.ModelAdmin):
    pass

class FiltroPreco(SimpleListFilter):
    title = "Preços"
    parameter_name = "Filtro Preço"

    def lookups(self, request, model_admin):
        return (('maior_60', 'Apartir de 60'),
                ('menor_60', 'Menor que 60'))

    def queryset(self, request, queryset):
        if self.value() == "maior_60":
            return queryset.filter(preco__gte=60)  # gte representa >= valor
        if self.value() == "menor_60":
            return queryset.filter(preco__lt=60)   # lt representa <= valor

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'categoria',)  # todos os campos que serão visto pelo usuário
    list_filter = ('categoria', FiltroPreco)                     # campos que viram filtros
    list_editable = ('preco',)                                   # Permite atualizar o objeto na listagem
    list_display_links = ('nome', 'descricao')                   # Link para saber toda descrição do produto
    search_fields = ('nome', 'descricao')                        # Permite pequisar pelos produtos
