from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Lab, LabResults
from .forms import LabResultsForm

# Create your views here.

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
		return Lab.objects.all()


class LabResultsDetails(ListView):
	model = LabResults
	template_name = 'healthy/results_detail.html'
	context_object_name = 'LabResults'

	@method_decorator(login_required)
	def dispach(self, *args, **kwargs):
		return super(LabResultsDetails, self).dispach(*args,**kwargs)


	def get_queryset(self):
<<<<<<< HEAD
		return LabResults.objects.all()

	#def get_object(self):
	#	return get_object_or_404(LabResults, pk=self.kwargs.get("pk"))
=======
		return Lab.objects.all()


class ProfilePage(ListView):
	template_name = 'healthy/profile.html'

	@method_decorator(login_required)
	def get(self, request):
		return render(request, self.template_name)


class AddLabResultPage(ListView):
	model = Lab
	template_name = 'healthy/addLab.html'
	success_url = '/labresults';
	form_class = LabResultsForm

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'labresultsform': form})
	
	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			self.object = form.save(commit=True)
			self.object.save()
			
			return redirect(self.success_url)
	
		return render(request, self.template_name, {'labresultsform': form})
>>>>>>> origin/master
