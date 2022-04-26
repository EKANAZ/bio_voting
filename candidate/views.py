from django.shortcuts import render
from user.models import User
# Create your views here
def first(request):
    obj=User.objects.all()
    details={
        'data':obj
    }
    return render(request,'candidate/first.html',details)
