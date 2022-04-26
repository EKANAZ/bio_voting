from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your view
import subprocess
from django.http import HttpResponseRedirect
def enroll(request):
    if request.method=="POST":
        subprocess.call(["d:\\client.bat"])
        return HttpResponseRedirect('/user/register/')

    return render(request,'user/callbatch.html')
def register(request):

    if request.method=="POST":

        # ss=request.POST.get('adr')
        # if User.objects.filter(adhdarcard=ss).exists():
        #
        #     ob=User.objects.filter(adhdarcard=ss).exists()
        #     msg="User already exists"
        #     context={
        #         'ok':msg,
        #     }
        #     return render(request,'user/register-form.html',context)
        # else:
        ob=User()
        ob.address=request.POST.get('address')
        ob.email=request.POST.get('useremail')
        ob.password=request.POST.get('userpassword')
        ob.confrim_password=request.POST.get('confirmpassword')
        ob.gender=request.POST.get('gender')
        ob.phone_number=request.POST.get('userphone')
        ob.username=request.POST.get('username')
        ob.status="Pending"
        # ob.adharcard=request.POST.get('adr')
        ob.save()
        obj=Login()
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('userpassword')
        obj.type="userp"
        obj.user_id=ob.u_id
        obj.save()
        return HttpResponseRedirect('/user/enroll/')
    return render(request,'user/register-form.html')

def verify(request):
    ob=User.objects.filter(status="Pending")


    context={
        'val':ob,

    }
    return render(request,'user/verify_user.html',context)
def viewuser(request):
    ob=User.objects.filter(status="verified")


    context={
        'val':ob,

    }
    return render(request,'user/delete.html',context)
def delete(request,idd):
    obj=User.objects.get(u_id=idd).delete()
    ob=Login.objects.get(user_id=idd).delete()

    return viewuser(request)

def verifyuser(request,idd):
    obj=Login.objects.get(user_id=idd,type='userp')
    obj.type="user"
    obj.save()
    ob=User.objects.get(u_id=idd)
    ob.status="verified"
    ob.save()
    return verify(request)