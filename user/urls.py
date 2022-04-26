from user import  views
from django.conf.urls import url

urlpatterns = [
url(r'^register/', views.register),
url(r'^verify/', views.verify),
url(r'^del/', views.viewuser),
    url('delete/(?P<idd>\w+)',views.delete,name="delus"),
    url('verfy/(?P<idd>\w+)',views.verifyuser,name="verfyuse"),
    url('enroll/',views.enroll),
]