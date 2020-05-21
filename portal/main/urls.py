from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_request, name='logout'),
    url(r'^$', views.login_request, name='login'),


]