# -*- coding: utf-8 -*-
from django.db import models
from application.fields import CIField, PhoneNumberField, CellPhoneNumberField
from application.models import ListaValor, ListaItem
from geoposition.fields import GeopositionField


class Postulante(models.Model):
    cedula = CIField("cédula de identidad", unique=True)
    nombres = models.CharField("nombres", max_length=30)
    apellidos = models.CharField("apellidos", max_length=30)
    fecha_nacimiento = models.DateField("fecha de nacimiento")
    estado_civil = models.ForeignKey(ListaItem, verbose_name="estado civil",
                                     limit_choices_to={"categoria_id": ListaValor.CAT_MARITAL_STATUS},
                                     to_field="codigo", on_delete=models.PROTECT,
                                     related_name="+")
    direccion = models.CharField("dirección", max_length=150, null=True, blank=True)
    localidad = models.ForeignKey(ListaItem, verbose_name="localidad",
                                  limit_choices_to={"categoria_id": ListaValor.CAT_LOCALITY},
                                  to_field="codigo", on_delete=models.PROTECT,
                                  null=True,
                                  related_name="+")
    telefono = PhoneNumberField("teléfono", null=True, blank=True,
                                help_text="Introduzca el número de teléfono")
    correo = models.EmailField("correo electrónico", null=True, blank=True)
    opinion_general = models.TextField("opinion general", max_length=100, null=True, blank=True,
                                  help_text="Opinión general respecto al postulante")

    informado = models.CharField("persona que informa", max_length=80, null=True)
    solicitante = models.CharField("persona que solicita", max_length=80, null=True)

    fecha_recoleccion = models.DateField("fecha de recolección")
    fecha_entrega = models.DateField("fecha de entrega")
    creado_en = models.DateTimeField("fecha de creación", editable=False, auto_now_add=True)

    class Meta:
        db_table = 'postulante'
        verbose_name = "postulante"
        verbose_name_plural = "postulantes"


class Salud(models.Model):
    postulante = models.OneToOneField(Postulante,verbose_name="postulante", related_name="salud",
                                      primary_key=True)
    seguro = models.ForeignKey(ListaItem, verbose_name="seguro médico",
                               limit_choices_to={'categoria_id': ListaValor.CAT_MEDICAL_ASSURANCE},
                               to_field="codigo", on_delete=models.PROTECT,
                               null=True, related_name="+", default="MEAS000")
    accidente = models.TextField("accidentes", max_length=100, null=True, blank=True)
    enfermedad = models.TextField("enfermedad grave", max_length=100, null=True, blank=True)
    convulsion = models.TextField("convulsiones", max_length=100, null=True, blank=True)
    bebida = models.ForeignKey(ListaItem, verbose_name="bebidas",
                               limit_choices_to={'categoria_id': ListaValor.CAT_FREQUENCY},
                               to_field="codigo", on_delete=models.PROTECT,
                               null=True, related_name="+")
    fuma = models.BooleanField("fuma", default=False)
    psicologico = models.TextField("tratamiento psicológico", max_length=100, null=True, blank=True)
    droga = models.TextField("drogas", max_length=100, null=True, blank=True)
    enf_frecuente = models.TextField("enfermedad frecuente", max_length=100, null=True, blank=True)
    medico = models.TextField("tratamiento médico", max_length=100, null=True, blank=True)
    control = models.BooleanField("control médico", default=False)

    class Meta:
        db_table = 'salud'
        verbose_name = "información de salud"
        verbose_name_plural = "información de salud"

class Convivencia(models.Model):
    postulante = models.OneToOneField(Postulante, verbose_name="postulante", related_name="convivencia",
                                      primary_key=True)
    evaluacion = models.TextField("evaluacion del grupo", max_length=100, null=True, blank=True,
                                  help_text="(vestimenta, higiene, relaciones interpersonales, hábitos)")

    class Meta:
        db_table = 'convivencia'
        verbose_name = "evaluación de grupo"
        verbose_name_plural = "evaluación de grupo"

class Relacion(models.Model):
    postulante = models.ForeignKey(Postulante, verbose_name="postulante", related_name="relaciones")
    nombre_apellido = models.CharField("nombres y apellidos", max_length=90)
    relacion = models.ForeignKey(ListaItem, verbose_name="relación",
                                 limit_choices_to={'categoria_id': ListaValor.CAT_RELATION},
                                 to_field="codigo", on_delete=models.PROTECT,
                                 null=True, related_name="+")
    edad = models.PositiveSmallIntegerField("edad", null=True, help_text="años")
    nacionalidad = models.ForeignKey(ListaItem, verbose_name="nacionalidad",
                                     limit_choices_to={'categoria_id': ListaValor.CAT_NATION},
                                     to_field="codigo", on_delete=models.PROTECT,
                                     null=True, related_name="+")
    ocupacion = models.CharField("ocupación", max_length=80, null=True, blank=True)

    class Meta:
        db_table = 'relacion'
        verbose_name = "familiar"
        verbose_name_plural = "familiares"


class Vivienda(models.Model):
    postulante = models.OneToOneField(Postulante, verbose_name="postulante", related_name="vivienda",
                                      primary_key=True)
    evaluacion = models.TextField("evaluación de vivienda", max_length=100, null=True, blank=True,
                                  help_text="(mobiliario, orden, limpieza)")
    construccion = models.CharField("tipo de construcción", max_length=100, null=True, blank=True)
    tenencia = models.CharField("tenencia", max_length=100, null=True, blank=True)
    tipo = models.CharField("tipo", max_length=100, null=True, blank=True)
    piezas = models.PositiveSmallIntegerField("número de piezas", null=True, blank=True)
    dormitorio = models.PositiveSmallIntegerField("número de dormitorios", null=True, blank=True)
    residuos = models.CharField("eliminación de residuos", max_length=100, null=True, blank=True)
    calle = models.CharField("calle", max_length=100, null=True, blank=True)
    agua = models.CharField("tipo de agua", max_length=100, null=True, blank=True)
    cant_sanitario = models.PositiveSmallIntegerField("total de sanitarios", null=True, blank=True)
    cocina = models.CharField("tipo de cocina", max_length=100, null=True, blank=True)
    alumbrado = models.CharField("tipo de alumbrado", max_length=100, null=True, blank=True)
    tipo_sanitario = models.CharField("tipo de sanitario", max_length=100, null=True, blank=True)
    desague = models.CharField("desagüe", max_length=100, null=True, blank=True)
    zona = models.CharField("zona", max_length=100, null=True, blank=True)
    proteccion = models.CharField("tipo de protección", max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'vivienda'
        verbose_name = "vivienda"
        verbose_name_plural = "viviendas"


class Expectativa(models.Model):
    postulante = models.OneToOneField(Postulante, verbose_name="postulante", related_name="expectativa",
                                      primary_key=True)
    evaluacion = models.TextField("situación actual", max_length=100, null=True, blank=True,
                                  help_text="situación actual, opinión y expectativas de ingreso")
    tiempo_translado = models.PositiveSmallIntegerField("tiempo de translado", help_text="minutos",
                                                        null=True, blank=True)
    disponibilidad = models.DateField("disponibilidad para ingreso", null=True, blank=True)
    transporte = models.ForeignKey(ListaItem, verbose_name="medio de transporte",
                                     limit_choices_to={'categoria_id': ListaValor.CAT_TRANSPORT},
                                     to_field="codigo", on_delete=models.PROTECT,
                                     null=True, related_name="+")
    parentesco = models.BooleanField("relación de parentesco", default=False,
                                     help_text="alguna relación de parentesco en la empresa")
    pretenciones = models.DecimalField("pretenciones salariales", decimal_places=0, max_digits=10,
                                       null=True, blank=True)

    class Meta:
        db_table = 'expectativa'
        verbose_name = "expectativas"
        verbose_name_plural = "expectativas"


class Pariente(models.Model):
    postulante = models.ForeignKey(Postulante, verbose_name="postulante", related_name="pariente")
    nombre_apellido = models.CharField("nombres y apellidos", max_length=90)
    relacion = models.TextField("relación",null=True, max_length=100)
    puesto = models.CharField("puesto", max_length=90, null=True)
    empresa = models.CharField("empresa", max_length=90, null=True)
    telefono = CellPhoneNumberField("teléfono", null=True)

    class Meta:
        db_table = 'pariente'
        verbose_name = "pariente"
        verbose_name_plural = "parientes"

class Conducta(models.Model):
    postulante = models.OneToOneField(Postulante, verbose_name="postulante", related_name="conducta",
                                      primary_key=True)
    personal = models.TextField("personales", max_length=100, null=True, blank=True)
    familiar = models.TextField("familiares", max_length=100, null=True, blank=True)
    pareja = models.TextField("pareja", max_length=100, null=True, blank=True,
                                  help_text="Aspectos de la relación")

    class Meta:
        db_table = 'conducta'
        verbose_name = "conducta"
        verbose_name_plural = "conductas"


class Referencia(models.Model):
    postulante = models.ForeignKey(Postulante, verbose_name="postulante", related_name="referencias")
    nombre_apellido = models.CharField("nombres y apellidos", max_length=90)
    telefono = CellPhoneNumberField("teléfono", null=True)
    relacion = models.ForeignKey(ListaItem, verbose_name="vinculo",
                                 limit_choices_to={'categoria_id': ListaValor.CAT_RELATION},
                                 to_field="codigo", on_delete=models.PROTECT,
                                 null=True, related_name="+")
    comentario = models.CharField("comentarios", max_length=80, null=True, blank=True)

    class Meta:
        db_table = 'referencia'
        verbose_name = "referencia personal"
        verbose_name_plural = "referencias personales"


class Ubicacion(models.Model):
    postulante = models.OneToOneField(Postulante, verbose_name="postulante", related_name="ubicacion",
                                      primary_key=True)
    posicion = GeopositionField("ubicación")

    class Meta:
        db_table = 'ubicacion'
        verbose_name = "ubicación de vivienda"
        verbose_name_plural = "ubicación de viviendas"