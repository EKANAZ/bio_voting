
from vote import  views
from django.conf.urls import url

urlpatterns = [
url(r'^cast_vote/', views.cast_vote),
url(r'^view result/', views.view),
]