from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from election_manifest.models import ElectionManifest
# Create your views here.
def post_election(request):
    if request.method=="POST":
        ob=ElectionManifest()
        ob.e_id="1"

        myfile = request.FILES['electionmanifest']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.manifest = myfile.name
        # ob.manifest=request.POST.get('electionmanifest')
        ob.save()
    return render(request,'election_manifest/post election manifest.html')
def view_post(request):
    obj=ElectionManifest.objects.all()
    print(obj)
    context ={
        'pos':obj
    }
    return render(request, "election_manifest/view_election_manifest.html", context)