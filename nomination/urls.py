from nomination import  views
from django.conf.urls import url

urlpatterns = [
    url(r'^mng/',views.viwn),
    url(r'^subnomi/',views.nami),
    url(r'^withdraw/', views.withdrawaappl),
    url('^withdraw_list/', views.withdraw_list),
    url(r'^wn_submit/(?P<idd>\w+)', views.wn_submit,name='wn_submit'),
    url(r'cadview/',views.cuview ),
    url(r'^approve/(?P<idd>\w+)',views.accept,name="accept"),
    url(r'^reject/(?P<idd>\w+)', views.reject, name="reject"),
    url(r'^accptwl/(?P<idd>\w+)', views.acceptwi, name="acceptwl"),
    url(r'^rejectwl/(?P<idd>\w+)', views.rejectwi, name="reject_wi"),


]