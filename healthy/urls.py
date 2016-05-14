from django.conf.urls import url
from . import views
from .views import LandingPage, HomePage, TestPage, LabResultsPage, ProfilePage, AddLabResultPage,AddLabPage

urlpatterns = [

    url(r'^$', LandingPage.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^home/$', HomePage.as_view(), name='home'),
    url(r'^test/$', TestPage.as_view(), name='test'),
    url(r'^labresults/$', LabResultsPage.as_view(), name='results'),
    url(r'^labresultsdetails/(?P<pk>\d+)$', LabResultsDetails.as_view(), name='results_detail'),
    # url(r'^addlab/$', AddLabResultPage.as_view(), name='add'),
    url(r'^profile/$', ProfilePage.as_view(), name='profile'),
    url(r'^addLab/$', AddLabPage.as_view(), name='addLab'),

]