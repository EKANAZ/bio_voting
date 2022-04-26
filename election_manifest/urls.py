from election_manifest import views
from django.conf.urls import url

urlpatterns = [
url(r'^post_election/', views.post_election),
    url('view_mani/',views.view_post)
]