from django.db import models
from django.utils.translation import ugettext_lazy as _

class ListaValor(models.Model):
    (CAT_MARITAL_STATUS,
     CAT_MEDICAL_ASSURANCE,
     CAT_TRANSPORT,
     CAT_RELATION,
     CAT_LOCALITY,
     CAT_FREQUENCY,
     CAT_NATION,
     ) = ('MAR', 'MEAS', 'TRAN', 'REL', 'LOC', 'FRQ', 'NTN')

    codigo = models.CharField(_("codigo"), max_length=4, primary_key=True,
                              help_text=_("Utilice una nomenclatura de al menos 3 letras"))
    nombre = models.CharField(_("nombre"), max_length=50)

    def __unicode__(self):
        return unicode("[%s] %s") % (self.codigo, self.nombre)

    class Meta:
        db_table = 'lista_valores'
        verbose_name = _("lista de valores")
        verbose_name_plural = _("listas de valores")
        ordering = ("codigo",)


class ListaItemManager(models.Manager):
    def get_by_natural_key(self, codigo):
        return self.get(codigo=codigo)


class ListaItem(models.Model):
    codigo = models.CharField(_("codigo"), db_index=True, max_length=10, unique=True, editable=False)
    etiqueta = models.CharField(_("etiqueta"), max_length=50)
    descripcion = models.CharField(_("descripcion"), max_length=100, null=True, blank=True)
    orden = models.PositiveIntegerField(_("orden"), default=0)
    categoria = models.ForeignKey(ListaValor, verbose_name=_("lista"), on_delete=models.CASCADE)

    objects = ListaItemManager()

    def __unicode__(self):
        return self.etiqueta

    def related_label(self):
        return self.etiqueta

    def save(self, *args, **kwargs):
        if self.codigo is None or self.codigo == "":
            try:
                qty = ListaItem.objects.filter(categoria=self.categoria_id).order_by('-codigo').values('codigo')[0]
                qty = int(qty.replace(self.categoria_id, "")) + 1
            except IndexError:
                qty = 1
            self.codigo = "%s%02d" % (self.categoria_id, qty)
            if self.orden is None or self.orden == 0:
                self.orden = qty
        super(ListaItem, self).save(*args, **kwargs)

    def natural_key(self):
        return self.codigo,

    class Meta:
        db_table = 'lista_item'
        verbose_name = _("item de lista")
        verbose_name_plural = _("items de lista")
        ordering = ("orden",)
