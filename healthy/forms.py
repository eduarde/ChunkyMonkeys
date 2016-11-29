from django import forms
from django.forms import HiddenInput
from datetimewidget.widgets import DateWidget
from .models import Lab, LabResults
from datetime import date, datetime, timedelta
from django.utils.timezone import now


class LabForm(forms.ModelForm):

	class Meta:
		model = Lab
		fields = ('date','ref_number','doctor','collection_point','patient_code')
		dateOptions = {
			'format': 'mm/dd/yyyy',
			'autoclose': True
		}
		widgets = {
			'date': DateWidget(attrs={'id':"iddata"}, bootstrap_version=3, options = dateOptions),
			'ref_number' : forms.NumberInput(attrs={'class': 'form-control'}),
			'doctor' : forms.TextInput(attrs={'class': 'form-control'}),
			'collection_point' : forms.TextInput(attrs={'class': 'form-control'}),
			'patient_code' : forms.NumberInput(attrs={'class': 'form-control'}),
        }


class LabResultsForm(forms.ModelForm):

	class Meta:
		model = LabResults
		fields = ('item_ref','value',)
		widgets = {
			'item_ref' : forms.Select(attrs={'class': 'form-control'}),
			'value' : forms.NumberInput(attrs={'class': 'form-control'}),
        }

