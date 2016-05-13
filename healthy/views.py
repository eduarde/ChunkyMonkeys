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

	@method_decorator(login_required)
	def dispach(self, *args, **kwargs):
		return super(LabResultsPage, self).dispach(*args,**kwargs)

	def get_queryset(self):
		return Lab.objects.all()

class ChartsPage(ListView):
	model = Lab
	template_name = 'healthy/charts.html'
	context_object_name = 'labs'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(charts, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		return Lab.objects.all().filter('user =', users.get_current_user())