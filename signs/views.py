from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.exceptions import MultipleObjectsReturned
from .models import User, Subject, Sign

def index(request):
    return render(request,'signs/index.html')

def showMondayTable(request):
    subjects = Subject.objects.all().filter(day=1)
    return render(request, 'signs/monday.html', {'subjects':subjects})

def showTuesdayTable(request):
    subjects = Subject.objects.all().filter(day=2)
    return render(request, 'signs/tuesday.html', {'subjects':subjects})

def showWednesdayTable(request):
    subjects = Subject.objects.all().filter(day=3)
    return render(request, 'signs/wednesday.html', {'subjects': subjects})

def showThursdayTable(request):
    subjects = Subject.objects.all().filter(day=4)
    return render(request, 'signs/thursday.html', {'subjects': subjects})

def showFridayTable(request):
    subjects = Subject.objects.all().filter(day=5)
    return render(request, 'signs/friday.html', {'subjects': subjects})


@login_required(login_url='/account/login/')
def signMe(request, subject_id):

    user = request.user
    subject = get_object_or_404(Subject, id=subject_id)
    sign = Sign()

    try:
        sign.user = user
        sign.subject = subject
        sign.subject.space = sign.subject.space +1
    except IntegrityError:
        raise MultipleObjectsReturned

    sign.save()
    return render(request, 'signs/sign_success.html', {'message': 'Success!'})

@login_required(login_url='/account/login/')
def mySigns(request):
    user = request.user
    subjects = Sign.objects.all().filter(user=user)
    return render(request, 'signs/my_signs.html', {'subjects': subjects})

@login_required(login_url='/account/login/')
def singMeOut(request, sign_id):
    user = request.user
    sign = Sign.objects.all().filter(id=sign_id)
    sign.delete()
    return render(request, 'signs/sign_out.html', {'message': 'You have been signed out successfully'})

