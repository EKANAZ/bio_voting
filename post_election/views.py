from django.shortcuts import render
from post_election.models import PostElection
# Create your views here.
def post_ele(request):
    if request.method=="POST":
        ob=PostElection()
        ob.e_id=request.POST.get('e_id')
        ob.p_id=request.POST.get('p_id')
        ob.post=request.POST.get('post')
        ob.save()
    return render(request,'post_election/post for election.html')
def view_post(request):
    object.PostElection()
    context ={
        'pos':object
    }
    return render(request,'post_election/view post.html',context)