from django.shortcuts import render, redirect

# from relMan.sex.forms import SexForm
import datetime
from .models import Sex
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def sex_view(request):
    sex_count = Sex.objects.filter(sex_user=request.user).count()
    check_sex = Sex.objects.all()
    if check_sex.exists():
        last_sex = Sex.objects.latest('created')
    else:
        last_sex = 0

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
    # sex = Sex.objects.filter(sex_user=request.user).latest('created')
    if Sex.objects.all().exists():
        sex = Sex.objects.filter(sex_user=request.user).latest('created')
        sex.delete()
    else:
        sex = 0
    return redirect('/sex-counter')
