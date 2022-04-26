from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login
# Create your views here.
def login(request):
    if request.method == "POST":
        un = request.POST.get("usr")
        ps = request.POST.get("pass")
        if Login.objects.filter(username=un, password=ps):
            obj = Login.objects.filter(username=un, password=ps)
            tp = ""
            for l in obj:
                tp = l.type
                uid = l.user_id
                if tp == "user":
                    request.session["uid"] = uid
                    return render(request,'temp/Public user.html')
                elif tp == "candidate":
                    request.session["uid"] = uid
                    return render(request,'temp/candidate.html')
                elif tp == "admin":
                     request.session["uid"] = uid
                     return render(request,'temp/index.html')
        else:
            obje = "Incorrect username or password!!!"
            context = {
                'inv': obje,
            }
    return render(request,'login/login.html')
