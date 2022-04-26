from django.shortcuts import render
from  result.models import Result
from result.models import Votting
from django.db.models import Count
import datetime
# Create your views here.
def publish_result(request):
    if request.method == "POST":
        result=Votting.objects.values('cand').order_by('cand').annotate(count=Count('cand'))
        for obj in result:
            ob=Result()
            ob.e_id=request.POST.get('e_id')
            ob.result=obj['count']
            ob.c_id=obj['cand']
            ob.time=datetime.datetime.now()
            ob.date=datetime.date.today()
            ob.save()
    return render(request,'result/publish result.html')

def candviewresult(request):
    objs=Result.objects.all()
    context={
        'oval':objs,
    }
    return render(request,'result/viewresult.html',context)

def candviewresultp(request):
    objs=Result.objects.all()
    context={
        'oval':objs,
    }
    return render(request,'result/viewresult1.html',context)