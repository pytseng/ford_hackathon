# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from .models import Spot


def index(request):
    all_spots = Spot.objects.all()
    # context = {'latest_question_list': latest_question_list}
    context = {'all_spots': all_spots}
    return render(request, 'parking/index.html', context)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'parking/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    


