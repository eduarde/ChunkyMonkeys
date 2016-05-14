from django.conf.urls import url
from . import views
from .views import LandingPage, HomePage, TestPage, LabResultsPage,LabResultsDetails

urlpatterns = [

    url(r'^$', LandingPage.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^home/$', HomePage.as_view(), name='home'),
    url(r'^test/$', TestPage.as_view(), name='test'),
    url(r'^labresults/$', LabResultsPage.as_view(), name='results'),
    url(r'^labresultsdetails/(?P<pk>\d+)$', LabResultsDetails.as_view(), name='results_detail'),

]