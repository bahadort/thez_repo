from django.shortcuts import render
from .models import Experiment


def experiment(request):
    exp_answers= Experiment.objects
    answer= request.POST.get('MyRadio')

    return render(request, 'experiment.html', {'experimental':exp_answers})
def question_2(request):
    answer=request.POST.get('MyRadio')
    return render(request, 'question-2.html', {'answer': answer})
def question_3(request):
    answer= request.POST.get('MyRadio')
    return render(request, 'question-3.html', {'answer': answer})
def refresh(request):
    answer= request.POST.get('MyRadio')
    return render(request, 'refresh.html', {'answer':answer})
