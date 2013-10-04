from django.contrib.admin import site, ModelAdmin
from suit.admin import SortableTabularInline
from .models import *
from jobapplicant.options import BaseOptions


class ListaItemInline(SortableTabularInline):
    model = ListaItem
    extra = 0
    sortable = 'orden'


class ListaValorOptions(BaseOptions, ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
    inlines = (ListaItemInline,)
    ordering = ("nombre",)

site.register(ListaValor, ListaValorOptions)