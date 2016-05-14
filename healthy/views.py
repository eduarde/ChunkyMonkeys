from django.shortcuts import render
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Lab, LabResults

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
		return LabResults.objects.all()

	#def get_object(self):
	#	return get_object_or_404(LabResults, pk=self.kwargs.get("pk"))