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

    # form = SexForm()

    # if request.method == 'POST':
    #     form = SexForm(request.POST or None)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.sex_user = request.user
    #         form.save()

    context = {
        'sex_count': sex_count,
        'current_user': request.user,
        'last_sex': last_sex
    }
    return render(request, 'sex/sex-counter.html', context)


@login_required
def addSex(request):
    # sex = Sex.objects.get(sex_user=request.user)

    # if request.method == 'POST':
    #     Sex.objects.create(sex_count=1)
    #     return redirect('/sex-counter')

    Sex.objects.create(sex_count=1, sex_user=request.user)

    return redirect('/sex-counter')


def deleteSex(request):
    sex = Sex.objects.filter(sex_user=request.user).latest('created')

    # if request.method == 'POST':
    #     sex.delete()
    #     return redirect('/sex-counter')

    sex.delete()
    return redirect('/sex-counter')
