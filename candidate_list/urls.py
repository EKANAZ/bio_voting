from candidate_list import views
from django.conf.urls import url

urlpatterns = [
    url(r'^view_candidate/', views.view_candidate),
    url(r'^viewcandidate/', views.view_cd),
]
