from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date, timedelta

class UserProfile(models.Model):
	F = 'F'
	M = 'M'

	GENDER_CHOICES = (
		(F, 'F'),
		(M, 'M'),
	)

	user = models.ForeignKey('auth.User', unique=True)
	gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default=F)
	dob = models.DateField('Date of birth',null=True)

	def __str__(self):
		return 'UserProfile ' + self.user

class Lab(models.Model):
	user = models.ForeignKey('auth.User', verbose_name='User', null=True)
	date = models.DateField('Date',blank=False, null=True)

	def __str__(self):
		return 'Lab ' + str(self.date)

class Item(models.Model):
	name = models.CharField('Name', max_length=20, blank=True, null=True)
	abbr = models.CharField('Abbreviation', max_length=10, blank=True, null=True)
	category = models.CharField('Category',max_length=20, blank=True, null=True)
	um = models.CharField('Unit', max_length=10, blank=False, null=False)

	def __str__(self):
		return 'Item ' + self.name

class LabResults(models.Model):
	user_ref = models.ForeignKey('auth.User')
	lab_ref = models.ForeignKey(Lab, related_name="Lab")
	item_ref = models.ForeignKey(Item,related_name="Item")
	value = models.DecimalField('Value', default=0, max_digits=3, decimal_places=2, null=True)

	def __str__(self):
		return 'LabResult ' + self.lab_ref

class LabGeneral(models.Model):
	user_ref = models.ForeignKey('auth.User')
	item_ref = models.ForeignKey(Item,related_name="ItemGeneral")
	threshold_min = models.DecimalField('Value', default=0, max_digits=3, decimal_places=2, null=True)
	threshold_max = models.DecimalField('Value', default=0, max_digits=3, decimal_places=2, null=True)

	def __str__(self):
		return 'LabGeneral ' + self.lab_ref


