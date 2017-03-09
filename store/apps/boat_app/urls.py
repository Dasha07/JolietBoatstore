from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #loads index page
<<<<<<< HEAD
    url(r'^contact$', views.contact), #loads contact page
    url(r'^contact/submit$', views.submit_contact_form), #runs submit_contact_form function in controller
    url(r'^test$', views.test)
=======
    url(r'^contact/$', views.contact), #loads contact page
    url(r'^contact/submit$', views.submit_contact_form) #runs submit_contact_form function in controller

>>>>>>> master
]
