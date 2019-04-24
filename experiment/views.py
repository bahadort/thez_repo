from django.shortcuts import render
from .models import Experiment
import psycopg2
import datetime
from . import inserter


def experiment(request):
    exp_answers= Experiment.objects
    answer = request.POST.get('MyRadio')
    return render(request, 'experiment.html', {'experimental':exp_answers})

    def insert(table, column, value):
        connection = psycopg2.connect(dbnam='thezdb', user='postgres', password='123456')
        mark = connection.cursor()
        statement = 'INSERT INTO ' + table + ' (' + column + ') VALUES (' + value + ')'
        mark.execute(statement)
        connection.commit()
        return
    inserted_data= insert('results', 'result_answerlr', answer)


def question_2(request):
    answer = str(request.POST.get('MyRadio'))
    inserter('results', 'result_answerlr', answer)
    return render(request, 'question-2.html', {'answer': answer})
def question_3(request):
    answer = str(request.POST.get('MyRadio'))
    inserter('results', 'result_answerlr', answer)
    return render(request, 'question-3.html', {'answer': answer})
def refresh(request):
    answer = str(request.POST.get('MyRadio'))
    inserter('results', 'result_answerlr', answer)
    return render(request, 'refresh.html', {'answer':answer})
