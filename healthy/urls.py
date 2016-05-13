from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^home/$', views.home, name='home'),

]