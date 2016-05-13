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
		return 'UserProfile ' + self.user.username

class Lab(models.Model):
	user = models.ForeignKey('auth.User', verbose_name='User', null=True)
	date = models.DateField('Date',blank=False, null=True)

	def __str__(self):
		return 'Lab ' + str(self.date)

class Item(models.Model):

	Leucocite = 'Leucocite(WBC)'
	Hematii = 'Hematii(RBC)'
	Hemoglobina = 'Hemoglobina(HGB)'
	VEM = 'VEM(volum eritocitar mediu)'
	HEM = 'HEM(hemoglobina eritocitara medie)'
	CHEM = 'CHEM(conc HB eritocitara medie)'
	RDW = 'RDW'
	Trombocite = 'Trombocite(PLT)'
	MPW = 'MPW'
	PDW = 'PDW'
	Neutro = 'Neutro'
	Lym = 'Lym'
	Monocite = 'Monocite'
	Eozinofile = 'Eozinofile'
	Bazofile = 'Bazofile'
	Creatinina = 'Creatinina serica'
	Magneziu = 'Magneziu seric'
	Sideremie = 'Sideremie'
	Glicemie = 'Glicemie'
	TGP = 'TGP'
	TSH = 'TSH'
	FT4 = 'FT4'

	NAME_CHOICES = (
		(Leucocite,'Leucocite'),
		(Hematii,'Hematii(RBC)'),
		(Hemoglobina,'Hemoglobina(HGB)'),
		(VEM,'VEM(volum eritocitar mediu'),
		(HEM,'HEM(hemoglobina eritocitara medie)'),
		(CHEM,'CHEM(conc HB eritocitara medie)'),
		(RDW, 'RDW'),
		(Trombocite,'Trombocite'),
		(MPW, 'MPW'),
		(PDW,'PDW'),
		(Neutro,'Neutro'),
		(Lym,'Lym'),
		(Monocite, 'Monocite'),
		(Eozinofile, 'Eozinofile'),
		(Bazofile, 'Bazofile'),
		(Creatinina,'Creatinina serica'),
		(Magneziu, 'Magneziu seric'),
		(Sideremie, 'Sideremie'),
		(Glicemie, 'Glicemie'),
		(TGP, 'TGP'),
		(TSH, 'TSH'),
		(FT4, 'FT4'),
	)

	Hematologie = 'Hematologie'
	Biochimie = 'Biochimie'
	Dozari = 'Dozari hormonale, Imunologie si markeri tumorali (Chemiluminiscenta)'

	CATEGORY_CHOICES = (
		(Hematologie, 'Hematologie'),
		(Biochimie, 'Biochimie'),
		(Dozari, 'Dozari hormonale, Imunologie si markeri tumorali (Chemiluminiscenta)'),

	)

	mm3 = '10^3/mm3'
	mm6 = '10^6/mm3'
	gdl = 'g/dl'
	percentage = '%'
	fL = 'fL'
	mgdl = 'mg/dl'
	UL = 'U\L'
	microUI = 'μUI\ml'
	ng = 'ng/dl'

	UM_CHOICES = (
		(mm3, '10^3/mm3'),
		(mm6, '10^6/mm3'),
		(gdl, 'g/dl'),
		(percentage, '%'),
		(fL, 'fL'),
		(mgdl, 'mg/dl'),
		(UL,'U\L'),
		(microUI, 'μUI\ml'),
		(ng, 'ng/dl'),
	)

	name = models.CharField('Name', max_length=20, blank=False, null=False, choices=NAME_CHOICES, default=Leucocite)
	abbr = models.CharField('Abbreviation', max_length=10, blank=True, null=True)
	category = models.CharField('Category',max_length=20, blank=False, null=False, choices=CATEGORY_CHOICES, default=Hematologie)
	um = models.CharField('Unit', max_length=10, blank=False, null=False, choices=UM_CHOICES,default=mm3)

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


