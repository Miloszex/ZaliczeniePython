#!/usr/bin/env python
# -- coding: utf-8 --

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.exceptions import MultipleObjectsReturned
from .models import User, Subject, Sign
from django.http import HttpResponse
import json


def index(request):
    return render(request,'signs/index.html')

def showMondayTable(request):
    user = request.user
    subjects = Subject.objects.all().filter(day=1)
    subjects_participation = {}

    try:
        for object in Subject.objects.all():
            if Sign.objects.all().filter(subject=object.id, user=user).exists():
                subjects_participation[object.id] = {'state': 'disabled', 'text': 'Zapisano'}
            else:
                subjects_participation[object.id] = {'state': ' ', 'text': 'Zapisz się'}
    except:
        pass

    return render(request, 'signs/monday.html', {'subjects':subjects, 'participation':subjects_participation})

def showTuesdayTable(request):
    user = request.user
    subjects = Subject.objects.all().filter(day=2)
    subjects_participation = {}

    try:
        for object in Subject.objects.all():
            if Sign.objects.all().filter(subject=object.id, user=user).exists():
                subjects_participation[object.id] = {'state': 'disabled', 'text': 'Zapisano'}
            else:
                subjects_participation[object.id] = {'state': ' ', 'text': 'Zapisz się'}
    except:
        pass

    return render(request, 'signs/tuesday.html', {'subjects': subjects, 'participation': subjects_participation})

def showWednesdayTable(request):
    user = request.user
    subjects = Subject.objects.all().filter(day=3)
    subjects_participation = {}

    try:
        for object in Subject.objects.all():
            if Sign.objects.all().filter(subject=object.id, user=user).exists():
                subjects_participation[object.id] = {'state': 'disabled', 'text': 'Zapisano'}
            else:
                subjects_participation[object.id] = {'state': ' ', 'text': 'Zapisz się'}
    except:
        pass

    return render(request, 'signs/wednesday.html', {'subjects': subjects, 'participation': subjects_participation})

def showThursdayTable(request):
    user = request.user
    subjects = Subject.objects.all().filter(day=4)
    subjects_participation = {}

    try:
        for object in Subject.objects.all():
            if Sign.objects.all().filter(subject=object.id, user=user).exists():
                subjects_participation[object.id] = {'state': 'disabled', 'text': 'Zapisano'}
            else:
                subjects_participation[object.id] = {'state': ' ', 'text': 'Zapisz się'}
    except:
        pass

    return render(request, 'signs/thursday.html.html', {'subjects': subjects, 'participation': subjects_participation})

def showFridayTable(request):
    user = request.user
    subjects = Subject.objects.all().filter(day=5)
    subjects_participation = {}

    try:
        for object in Subject.objects.all():
            if Sign.objects.all().filter(subject=object.id, user=user).exists():
                subjects_participation[object.id] = {'state': 'disabled', 'text': 'Zapisano'}
            else:
                subjects_participation[object.id] = {'state': ' ', 'text': 'Zapisz się'}
    except:
        pass

    return render(request, 'signs/friday.html', {'subjects': subjects, 'participation': subjects_participation})


@login_required(login_url='/account/login/')
def signMe(request, subject_id):

    user = request.user
    subject = get_object_or_404(Subject, id=subject_id)
    sign = Sign()


    try:
        sign.user = user
        sign.subject = subject
    finally:
        if subject.actual_space < subject.space:
            subject.actual_space = subject.actual_space + 1
            subject.save()
            sign.save()
        else:
            pass

    if Sign.objects.all().filter(subject=subject.id, user=user).exists():
        response = {'answer': 'Pomyślnie zapisano'}
    else:
        response = {'answer': 'Nie udało się zapisać'}

    return HttpResponse(json.dumps(response), content_type='application/json')

@login_required(login_url='/account/login/')
def mySigns(request):
    user = request.user
    subjects = Sign.objects.all().filter(user=user)
    return render(request, 'signs/my_signs.html', {'subjects': subjects})

@login_required(login_url='/account/login/')
def singMeOut(request, sign_id):
    sign = get_object_or_404(Sign, id=sign_id)
    sign.subject.actual_space = sign.subject.actual_space-1
    sign.subject.save()
    sign.delete()

    return render(request, 'signs/sign_out.html', {'message': 'You have been signed out successfully'})
