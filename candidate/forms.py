from django.forms import ModelForm
from suit.widgets import *


class RelacionForm(ModelForm):

    class Meta:
        widgets = {
            'edad': NumberInput(attrs={'class': 'input-mini'}),
            'relacion': Select(attrs={'class': 'input-small'}),
            'nacionalidad': Select(attrs={'class': 'input-medium'}),
            'ocupacion': TextInput(attrs={'class': 'input-medium'})
        }
