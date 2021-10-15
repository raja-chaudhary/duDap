from django.shortcuts import render, redirect

# from relMan.sex.forms import SexForm
import datetime
from .models import Sex
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def sex_view(request):
    sex_count = Sex.objects.filter(sex_user=request.user).count()
    last_sex = Sex.objects.latest('created')

    context = {
        'sex_count': sex_count,
        'current_user': request.user,
        'last_sex': last_sex
    }
    return render(request, 'sex/sex-counter.html', context)


@login_required
def addSex(request):

    Sex.objects.create(sex_count=1, sex_user=request.user)

    return redirect('/sex-counter')


@login_required
def deleteSex(request):
    sex = Sex.objects.filter(sex_user=request.user).latest('created')

    sex.delete()
    return redirect('/sex-counter')
