from django.shortcuts import render
from nomination.models import Nomination
from nomination.models import Nomni
from candidate_list.models import CandidateList
from nomination.models import Withdraw
from login.models import Login
from election.models import Election
# Create your views here.
def viwn (request):

    object=Nomni.objects.filter(status="pending")
    context = {
        'val': object

    }

    return render(request,'nomination/manage nomination.html',context)
def accept(request,idd):
    obj=Nomni.objects.get(n_id=idd)
    obj.status="approved"
    obj.save()
    objc=CandidateList()
    objc.position=obj.position
    objc.n_id=idd
    objc.candidate_name=obj.name
    objc.status='candidate'
    objc.save()
    oo=Login.objects.get(user_id=obj.u_id)
    oo.type='candidate'
    oo.save()
    return viwn(request)


def reject(request,idd):
    obj=Nomni.objects.get(n_id=idd)
    obj.status="rejected"
    obj.save()
    return viwn(request)

def nami(requset):
    dd=requset.session["uid"]
    bb=Election.objects.all()
    context={
        'pp':bb
    }
    if requset.method =="POST":
        object=Nomni()
        object.u_id=dd
        object.name=requset.POST.get('cn')
        object.position=requset.POST.get('cp')
        object.place=requset.POST.get('cpl')
        object.status='pending'
        object.save()
    return render(requset,'nomination/submit nomination.html',context)

# def submit(request):
#     if request.method=="POST":
#         ob=Nomination()
#         ob.e_id=request.POST.get('e_id')
#         ob.p_id=request.POST.get('post')
#         ob.c_id="1"
#         ob.n_id="1"
#         ob.status="1"
#         ob.save()
#     return render(request,'nomination/submit nomination.html')

def withdrawaappl(request):
    vv=request.session["uid"]
    ob=Nomni.objects.filter(u_id=vv)
    con={
        'ooop':ob
    }
    return render(request,'nomination/withdraw nomination.html',con)

def wn_submit(request,idd):
    ss= request.session["uid"]
    if request.method=="POST":
        obj=Withdraw()
        obj.n_id=idd
        obj.u_id=ss
        obj.reason=request.POST.get('reson')
        obj.withdraw_status="withdraw"
        obj.save()
    return render(request,'nomination/wn_submit.html')
def cuview (request):

    object=Nomni.objects.all()
    context = {
        'val': object

    }

    return render(request,'nomination/cadview.html',context)

def withdraw_list (request):
    object=Withdraw.objects.filter(withdraw_status='withdraw')
    context={
        'ok':object
    }
    return render(request,'nomination/witdraw_list.html',context)
def acceptwi(request,idd):
    obj=Withdraw.objects.get(w_id=idd)
    obj.withdraw_status="approved"
    obj.save()
    oo=CandidateList.objects.get(n_id=obj.n_id)
    oo.status='withdraw'
    oo.save()
    oc=CandidateList.objects.filter(status="withdraw")

    ok=Login.objects.get(user_id=obj.u_id)
    ok.type="user"
    ok.save()
    # objc=CandidateList.objects.filter(cl_id=obj.n_id).delete()

    return withdraw_list(request)


def rejectwi(request,idd):
    obj=Withdraw.objects.get(w_id=idd)
    obj.withdraw_status="rejected"
    obj.save()
    return withdraw_list(request)