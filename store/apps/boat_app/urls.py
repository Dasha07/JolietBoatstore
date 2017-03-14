from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #loads index page
    url(r'^contact/$', views.contact), #loads contact page
    url(r'^contact/submit$', views.submit_contact_form), #runs submit_contact_form function in controller
    url(r'^transport/$', views.transport), #loads transportation page
    url(r'^shore/$', views.shore), #loads shore power page
    url(r'^waste/$', views.waste) #loads waste page

]
