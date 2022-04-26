from django.shortcuts import render
from django.db.models import Count
from vote.models import Votting

# Create your views here.
def cast_vote(request):
    if request.method=="POST":
        ob=Votting()
        ob.e_id=request.POST.get('e_id')
        ob.c_id=request.POST.get('c_id')
        ob.p_id=request.POST.get('p_id')
        ob.v_id="1"
        ob.save()
    return render(request,'vote/cast vote.html')

def view(request):
    obj=Votting.objects.all()
    context={
        'ok':obj
    }

    return render(request,'vote/view result.html',context)