"""bio_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('login/',include('login.urls')),
    url('candidate/',include('candidate.urls')),
    url('candidate_list/', include('candidate_list.urls')),
    url('election/', include('election.urls')),
    url('election_manifest/', include('election_manifest.urls')),
    url('nomination/', include('nomination.urls')),
    url('post_election/', include('post_election.urls')),
    url('result/', include('result.urls')),
    url('user/', include('user.urls')),
    url('vote/', include('vote.urls')),
    url('temp/',include('temp.url')),
    url('$',views.login),

]
