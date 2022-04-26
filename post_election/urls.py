from post_election import views
from django.conf.urls import url

urlpatterns = [
url(r'^post_ele/', views.post_ele),
url(r'^view_election/', views.view_post),
]