from login import  views
from django.conf.urls import url

urlpatterns = [

url(r'^login/', views.login),
]