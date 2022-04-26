from django.shortcuts import render

# Create your views here.
def ad(request):
    return render(request,'temp/index.html')
def cd(request):
    return render(request,'temp/candidate.html')
def pu(request):
    return render(request,'temp/Public user.html')
