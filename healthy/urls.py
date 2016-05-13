from django.conf.urls import url
from . import views
from .views import LandingPage, HomePage

urlpatterns = [

    url(r'^$', LandingPage.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^home/$', HomePage.as_view(), name='home'),

]