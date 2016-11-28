from django import forms
from django.forms import HiddenInput
from datetimewidget.widgets import DateWidget
from .models import Lab, LabResults, LabDetail
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
		widgets = {
			'item_ref' : forms.Select(attrs={'class': 'form-control'}),
			'value' : forms.NumberInput(attrs={'class': 'form-control'}),
        }

class LabDetailForm(forms.ModelForm):

	class Meta:
		model = LabDetail
		fields = ('reason', 'cause' , 'action',)
		widgets = {
			'reason' : forms.TextInput(attrs={'class': 'form-control'}),
			'cause' : forms.TextInput(attrs={'class': 'form-control'}),
			'action' : forms.TextInput(attrs={'class': 'form-control'}),
        }