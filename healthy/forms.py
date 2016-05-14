from django import forms
from django.forms import HiddenInput
from datetimewidget.widgets import DateWidget
from .models import Lab, LabResults
from datetime import date, datetime, timedelta
from django.utils.timezone import now


class LabForm(forms.ModelForm):

	class Meta:
		model = Lab
		fields = ('date',)
		dateOptions = {
			'format': 'mm/dd/yyyy',
			'autoclose': True
		}
		widgets = {
			'date': DateWidget(attrs={'id':"iddata"}, bootstrap_version=3, options = dateOptions),
        }

class LabResultsForm(forms.ModelForm):

	class Meta:
		model = LabResults
		fields = ('item_ref','value',)
		dateOptions = {
			'format': 'mm/dd/yyyy',
			'autoclose': True
		}
		widgets = {
			'item_ref': forms.Select(attrs={'class': 'form-control'}),
			'value': forms.NumberInput(attrs={'class': 'form-control'}),
        }