from result import  views
from django.conf.urls import url

urlpatterns = [
    url(r'^publish_result/', views.publish_result),
    url(r'^cresult/', views.candviewresult),
url(r'^presult/', views.candviewresultp),
]