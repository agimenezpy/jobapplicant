# -*- coding: utf-8 -*-
from django.contrib.admin import site, ModelAdmin, StackedInline, TabularInline, HORIZONTAL
from .models import Postulante, Salud, Convivencia, Relacion, Vivienda, Expectativa, Conducta, Pariente, Referencia, Ubicacion
from .forms import RelacionForm
from jobapplicant.options import BaseOptions
from django.db import models
from suit.widgets import AutosizedTextarea


class SaludInline(BaseOptions, StackedInline):
    model = Salud
    can_delete = False
    suit_classes = 'suit-tab suit-tab-salud'
    radio_fields = {'bebida': HORIZONTAL}

    formfield_overrides = {
        models.TextField: {'widget': AutosizedTextarea(attrs={
            'rows': 2,
            'class': 'input-normal',
            'max-height': '100px',
        })},
    }


class ConvivenciaInline(BaseOptions, StackedInline):
    model = Convivencia
    can_delete = False
    suit_classes = 'suit-tab suit-tab-grupo'
    fieldsets = (
        (None, {
            'classes': ('full-width',),
            'fields': ('evaluacion',)
        }),
    )


class ViviendaInline(BaseOptions, StackedInline):
    model = Vivienda
    can_delete = False
    suit_classes = 'suit-tab suit-tab-vivienda'
    fieldsets = (
        (None, {
            'classes': ('full-width',),
            'fields': ('evaluacion',)
        }),
        ("Características, ubicación y servicios", {
            'fields': (
                'construccion', 'tenencia', 'tipo',
                'piezas', 'dormitorio', 'residuos',
                'calle', 'agua', 'cant_sanitario',
                'cocina', 'alumbrado', 'tipo_sanitario',
                'desague', 'zona', 'proteccion',
            )
        })
    )


class RelacionInline(TabularInline):
    form = RelacionForm
    model = Relacion
    suit_classes = 'suit-tab suit-tab-grupo'
    extra = 0
    max_num = 5


class ExpectativaInline(BaseOptions, StackedInline):
    model = Expectativa
    can_delete = False
    suit_classes = 'suit-tab suit-tab-expectativa'
    fieldsets = (
        (None, {
            'fields': (
                'tiempo_translado', 'disponibilidad', 'transporte',
                'parentesco', 'pretenciones',
            )
        }),
        ("Situación actual", {
            'classes': ('full-width',),
            'fields': ('evaluacion',)
        })
    )


class ParienteInline(TabularInline):
    model = Pariente
    suit_classes = 'suit-tab suit-tab-expectativa'
    extra = 0
    max_num = 5


class ConductaInline(BaseOptions, StackedInline):
    model = Conducta
    can_delete = False
    suit_classes = 'suit-tab suit-tab-conducta'
    formfield_overrides = {
        models.TextField: {'widget': AutosizedTextarea(attrs={
            'rows': 5,
            'class': 'input-normal',
            'max-height': '100px',
        })},
    }


class ReferenciaInline(TabularInline):
    model = Referencia
    suit_classes = 'suit-tab suit-tab-conducta'
    extra = 0
    max_num = 5


class UbicacionInline(BaseOptions, StackedInline):
    model = Ubicacion
    can_delete = False
    suit_classes = 'suit-tab suit-tab-ubicacion'


class PostulanteOptions(BaseOptions, ModelAdmin):
    list_display = ('cedula', 'full_name')
    list_display_links = ('cedula',)
    inlines = (SaludInline, ExpectativaInline, ParienteInline, RelacionInline,
               ConvivenciaInline, ViviendaInline, ConductaInline, ReferenciaInline, UbicacionInline)

    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('cedula', 'nombres', 'apellidos',
                       'fecha_nacimiento', 'estado_civil',)
        }),
        ("Contacto", {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('direccion', 'localidad', 'telefono', 'correo',)
        }),
        ("Entrevista", {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('informado', 'solicitante', 'fecha_recoleccion', 'fecha_entrega'),
        }),
        ("Opinión general", {
            'classes': ('suit-tab suit-tab-general full-width',),
            'fields': ('opinion_general',)
        }),
    )

    suit_form_tabs = (
        ('general', "Datos personales"),
        ('salud', "Información de salud"),
        ('expectativa', "Expectativas de ingreso"),
        ('grupo', "Acerca del grupo conviviente"),
        ('vivienda', "Situación de Vivienda"),
        ('conducta', "Conductas"),
        ('ubicacion', "Mapa de ubicación"),
    )

    def full_name(self, object):
        return "%s, %s" % (object.nombres, object.apellidos)
    full_name.short_description = "nombre completo"
    full_name.admin_order_Field = "apellidos"

site.register(Postulante, PostulanteOptions)