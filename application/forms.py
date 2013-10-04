from django.forms.fields import RegexField
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from string import join
from django.utils.translation import ugettext_lazy as _

class PYPhoneNumberField(RegexField):
    default_error_messages = {
        'invalid': _("El numero debe estar en el formato (XXXX) XXX-XXXX o XXX-XXXX"),
    }

    def __init__(self, max_length=15, min_length=3, *args, **kwargs):
        super(PYPhoneNumberField, self).__init__("^(\(\d{3,4}\) )?(\d{3}-)?\d{3,4}$",
                                                 max_length, min_length, *args, **kwargs)

    def clean(self, value):
        super(PYPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return u''
        return value


class PYCellPhoneNumberField(RegexField):
    default_error_messages = {
        'invalid': _("El numero debe estar en el formato (XXXX) XXX-XXX"),
    }

    def __init__(self, max_length=14, min_length=14, *args, **kwargs):
        super(PYCellPhoneNumberField, self).__init__("^\(09[9876]\d\) \d{3}-\d{3}$", max_length,
                                                     min_length, *args, **kwargs)

    def clean(self, value):
        super(PYCellPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return u''
        return value


class PYCIField(RegexField):
    """
    A field that validates 'Documento Nacional de Identidad' (DNI) numbers.
    """
    default_error_messages = {
        'invalid': _("El numero de cedula es invalido.")
    }

    def __init__(self, max_length=10, min_length=1, *args, **kwargs):
        super(PYCIField, self).__init__("^\d+[a-z]?$", max_length, min_length, *args, **kwargs)

    def clean(self, value):
        """
        Value can be a string either in the [X]X.XXX.XXX or [X]XXXXXXX formats.
        """
        value = super(PYCIField, self).clean(value)
        if value in EMPTY_VALUES:
            return u''

        return value


class PYRUCField(RegexField):
    """
    This field validates a RUC (Registro Unico de Contribuyentes). A RUC is of
    the form XXXXXXXX-X.
    """
    default_error_messages = {
        'invalid': _("Ingrese un RUC valido en el formato XXXXXXXX-X."),
        'checksum': _("RUC invalido"),
    }

    def __init__(self, max_length=10, min_length=3, *args, **kwargs):
        super(PYRUCField, self).__init__(r'^\d{1,8}-\d$',
                                         max_length, min_length, *args, **kwargs)

    def clean(self, value):
        """
        Value can be a string in the format XXXXXXXX-X
        """
        value = super(PYRUCField, self).clean(value)
        if value in EMPTY_VALUES:
            return u''
        value, cd = self._canon(value)
        if self._calc_cd(value) != cd:
            raise ValidationError(self.error_messages['checksum'])
        return self._format(value, cd)

    def _canon(self, ruc):
        ruc = ruc.replace('-', '')
        return ruc[:-1], int(ruc[-1], 10)

    def _calc_cd(self, ruc, basemax=11):
        ruc = join(map(str,[(i if ord(i) >= 48 and ord(i) <= 57 else ord(i)) for i in ruc.upper()]), "")
        k = 2
        total = 0
        for i in range(0, len(ruc)):
            if k > basemax:
                k = 2
            numero_aux = int(ruc[-(i+1)],10)
            total += (numero_aux * k)
            k += 1

        resto = total % 11
        return 11 - resto if resto > 1 else 0

    def _format(self, ruc, check_digit=None):
        if check_digit is None:
            check_digit = ruc[-1]
            ruc = ruc[:-1]
        return u'%s-%s' % (ruc, check_digit)


class GlobalBarcodeField(RegexField):
    """
    A field that validates 'Barcode' numbers.
    """
    default_error_messages = {
        'invalid': _("El codigo de barras es invalido.")
    }

    def __init__(self, max_length=12, min_length=8, *args, **kwargs):
        super(GlobalBarcodeField, self).__init__("^\d{8,12}$", max_length, min_length,
                                                 *args, **kwargs)

    def clean(self, value):
        """
        Value can be a string either in the XXXXXXXXXXXX or XXXXXXXX formats.
        """
        value = super(GlobalBarcodeField, self).clean(value)
        if value in EMPTY_VALUES:
            return u''

        return value
