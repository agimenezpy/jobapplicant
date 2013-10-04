from django.db import models
from suit.widgets import SuitDateWidget, SuitSplitDateTimeWidget, NumberInput
from suit_redactor.widgets import RedactorWidget


class BaseOptions(object):
    list_per_page = 15

    formfield_overrides = {
        models.DateField: {'widget': SuitDateWidget},
        models.DateTimeField: {'widget': SuitSplitDateTimeWidget},
        models.PositiveSmallIntegerField: {'widget': NumberInput(attrs={'class': 'input-mini'})},
        models.TextField: {'widget': RedactorWidget(editor_options={'lang':'es'})}
    }
