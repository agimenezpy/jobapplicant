from django.db.models.fields import CharField
from .forms import (PYCIField, PYRUCField, PYPhoneNumberField, PYCellPhoneNumberField, GlobalBarcodeField)
from django.utils.translation import ugettext_lazy as _


class CIField(CharField):
    description = _("cedula")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(CIField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': PYCIField}
        defaults.update(kwargs)
        return super(CIField, self).formfield(**defaults)


class RUCField(CharField):
    description = _("RUC")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(RUCField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': PYRUCField}
        defaults.update(kwargs)
        return super(RUCField, self).formfield(**defaults)


class PhoneNumberField(CharField):
    description = _("telefono")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 15
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': PYPhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)


class CellPhoneNumberField(CharField):
    description = _("telefono celular")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        super(CellPhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': PYCellPhoneNumberField}
        defaults.update(kwargs)
        return super(CellPhoneNumberField, self).formfield(**defaults)


class BarcodeField(CharField):
    description = _("codigo de barras")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 12
        super(BarcodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': GlobalBarcodeField}
        defaults.update(kwargs)
        return super(BarcodeField, self).formfield(**defaults)
