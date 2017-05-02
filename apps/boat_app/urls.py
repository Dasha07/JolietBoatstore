from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #loads index page
    url(r'^contact/$', views.contact), #loads contact page
    url(r'^contact/submit$', views.submit_contact_form), #runs submit_contact_form function in controller
    url(r'^transport/$', views.transport), #loads transportation page
    url(r'^shore/$', views.shore), #loads shore power page
    url(r'^water_fuel/$', views.water_fuel), #loads water fuel page
    url(r'^grocery_supply/$', views.groceries), #loads supplies and groceries page
    url(r'^waste/$', views.waste), #loads waste page
    url(r'^points/$', views.points) #loads points of interest page
]
