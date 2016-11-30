from django.conf.urls import url
from . import views
from .views import LandingPage, HomePage, LabResultsPage, ProfilePage, AddLabResultsPage,AddLabPage, LabResultsDetails, ChartsPage, DictionaryPage, DictionaryItem

urlpatterns = [

    url(r'^$', LandingPage.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^home/$', HomePage.as_view(), name='home'),
    url(r'^labresults/$', LabResultsPage.as_view(), name='results'),
    url(r'^labresultsdetails/(?P<pk>\d+)$', LabResultsDetails.as_view(), name='results_detail'),
    url(r'^charts/$', ChartsPage.as_view(), name='charts'),
    url(r'^dictionary/$', DictionaryPage.as_view(), name='dictionary'),
    url(r'^dictionaryItem/(?P<pk>\d+)$', DictionaryItem.as_view(), name='dictionary_item'),
    url(r'^profile/$', ProfilePage.as_view(), name='profile'),
    url(r'^addLab/$', AddLabPage.as_view(), name='addLab'),
    url(r'^addLabResults/(?P<pk>\d+)$', AddLabResultsPage.as_view(), name='addLabResults'),

]