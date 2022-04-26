from election import  views
from django.conf.urls import url

urlpatterns = [
    url(r'^election/', views.election),
    url(r'^view_election/', views.view_election),
]