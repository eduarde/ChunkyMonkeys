from django.conf.urls import url
from . import views
from .views import AddLabDetailPage, LabDetailPage, LandingPage, HomePage, TestPage, LabResultsPage, ProfilePage, AddLabResultsPage,AddLabPage, LabResultsDetails, ChartsPage

urlpatterns = [

    url(r'^$', LandingPage.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^home/$', HomePage.as_view(), name='home'),
    url(r'^test/$', TestPage.as_view(), name='test'),
    url(r'^labresults/$', LabResultsPage.as_view(), name='results'),
    url(r'^labresultsdetails/(?P<pk>\d+)$', LabResultsDetails.as_view(), name='results_detail'),
    url(r'^charts/$', ChartsPage.as_view(), name='charts'),
    url(r'^profile/$', ProfilePage.as_view(), name='profile'),
    url(r'^addLab/$', AddLabPage.as_view(), name='addLab'),
    url(r'^addLabResults/(?P<pk>\d+)$', AddLabResultsPage.as_view(), name='addLabResults'),

    url(r'^addlabdetail/(?P<pk>\d+)$', AddLabDetailPage.as_view(), name='add_lab_detail'),
    url(r'^labdetail/(?P<pk>\d+)$', LabDetailPage.as_view(), name='lab_detail'),


]