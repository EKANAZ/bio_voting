from django.shortcuts import render
from candidate_list.models import CandidateList
from nomination.models import Nomni


# Create your views here.
def view_candidate(request):
    obj = CandidateList.objects.filter(status="candidate")
    context = {
        'ok': obj
    }

    return render(request, 'candidate_list/view candidate list.html', context)


def view_cd(request):
    obj = CandidateList.objects.filter(status="candidate")
    context = {
        'ok': obj
    }

    return render(request, 'candidate_list/candidatelistbycand.html', context)
