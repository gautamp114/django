from django.shortcuts import render

from .models import Question

import time

import random

from django.http import JsonResponse


global values
values = []
def home(request):
    qstn = Question.objects.all().count()
    # a = ""
    num = ''
    # print(values, "dfsljf ")
    def generator():
        num = random.randint(1,qstn)
        return num

    if len(values) == 0:
        a = generator()
    # print(len(values))
    if a in values:
        a = generator()
    else:
        a = generator()
        # values.append(a)
        print('hello')
        print(values)
        query = Question.objects.get(id = a)

    if request.method == "POST":
        # print('sfsf')
        return JsonResponse('j', safe=False)
    
    
    context = {
        'query' : query,
    }
    template = 'quiz.html'
    return render(request, template, context)
