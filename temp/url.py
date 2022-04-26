from temp import  views
from django.conf.urls import url

urlpatterns = [
url('temad/', views.ad),
url('candidate/', views.cd),
url('publicuser/', views.pu),

]