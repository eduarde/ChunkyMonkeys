from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'healthy/index.html', {})

def home(request):
	return render(request, 'healthy/home.html' , {})