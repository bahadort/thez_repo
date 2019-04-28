from django.shortcuts import render
from .models import Experiment
import psycopg2
import datetime



def experiment(request):

    return render(request, 'exp.html')
def question_2(request):
    answer = str(request.POST.get('MyRadio'))

    return render(request, 'question-2.html', {'answer': answer})
def question_3(request):
    answer = str(request.POST.get('MyRadio'))

    return render(request, 'question-3.html', {'answer': answer})
def refresh(request):
    answer = str(request.POST.get('MyRadio'))

    return render(request, 'refresh.html', {'answer':answer})
