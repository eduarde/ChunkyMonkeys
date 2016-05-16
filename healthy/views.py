from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from .models import Lab, LabResults, LabGeneral
from .forms import LabForm, LabResultsForm


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

class LandingPage(View):
	template_name = 'healthy/index.html'

	def get(self, request):
		return render(request, self.template_name)

class HomePage(View):
	template_name = 'healthy/home.html'

	@method_decorator(login_required)
	def get(self, request):
		return render(request, self.template_name)


class TestPage(ListView):
	model = Lab
	template_name = 'healthy/test.html'
	context_object_name = 'labs'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TestPage, self).dispatch(*args, **kwargs)
	
	def get_queryset(self):
		return Lab.objects.all()

class LabResultsPage(ListView):
	model = Lab
	template_name = 'healthy/labresults.html'
	context_object_name = 'results'

	
	def get_queryset(self):
		return Lab.objects.all().filter(user=self.request.user)


class LabResultsDetails(ListView):
	model = LabResults
	template_name = 'healthy/results_detail.html'
	context_object_name = 'LabResults'

	@method_decorator(login_required)
	def dispach(self, *args, **kwargs):
		return super(LabResultsDetails, self).dispach(*args,**kwargs)

	def get_object(self):
		return get_object_or_404(Lab, pk=self.kwargs.get("pk"))	

	def get_queryset(self):
		return LabResults.objects.all().filter(lab_ref=self.get_object())


class ProfilePage(ListView):
	template_name = 'healthy/profile.html'

	@method_decorator(login_required)
	def get(self, request):
		return render(request, self.template_name)


class AddLabPage(ListView):
	model = Lab
	template_name = 'healthy/addLab.html'
	success_url = '/labresults';
	form_class = LabForm

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'labresultsform': form})
	
	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=False)
			self.object.user = self.request.user
			self.object.save()
			
			return redirect(self.success_url)
	

class AddLabResultsPage(ListView):
	model = LabResults
	template_name = 'healthy/addLabResults.html'
	success_url = '/labresults';
	form_class = LabResultsForm

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):	
		form = self.form_class()
		return render(request, self.template_name, {'labresultsform': form})

	def get_object(self):
		return get_object_or_404(Lab, pk=self.kwargs.get("pk"))

	def get_lab_general(self,item_name):
	 	return LabGeneral.objects.get(item_ref__name=item_name)
	
	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=False)
			self.object.user_ref = self.request.user
			self.object.lab_ref = self.get_object()
			self.object.general_ref = self.get_lab_general(self.object.item_ref.name)
			self.object.save()
			return redirect(self.success_url)
	
		return render(request, self.template_name, {'labresultsform': form})


class ChartsPage(View):
	template_name = 'healthy/charts.html'

	def get(self, request):
		return render(request, self.template_name)