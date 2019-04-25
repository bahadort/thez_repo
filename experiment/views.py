from django.shortcuts import render
from .models import Experiment
import psycopg2
import datetime



def experiment(request):
    exp_answers= Experiment.objects
    answer = request.POST.get('MyRadio')
    connection= psycopg2.connect(database='thezdb',
                                 user='postgres',
                                 password='123456',
                                 host = "104.248.253.111",
                                 port = "5432")
    mark = connection.cursor()
    table = 'results'
    column = 'result_answerlr'
    value = answer
    statement = 'INSERT INTO ' + table + ' (' + column + ') VALUES (' + value + ')'
    mark.execute(statement)
    connection.commit()
    mark.close()
    connection.close()


    return render(request, 'experiment.html', {'experimental': exp_answers})


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
