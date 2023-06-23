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

