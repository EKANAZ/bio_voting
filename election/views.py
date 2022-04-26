from django.shortcuts import render
from election.models import Election
# Create your views here.
def election(request):
    if request.method=="POST":
        ob=Election()
        ob.e_id=request.POST.get('e_id')
        ob.election=request.POST.get('election')
        ob.date=request.POST.get('date')
        ob.save()
    return render(request,'election/election.html')
def view_election(request):
    ob = Election.objects.all()
    context = {
        'val': ob
    }

    return render(request,'election/view_election.html',context)