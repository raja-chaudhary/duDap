from django.shortcuts import render, redirect

from relMan.sex.forms import SexForm
from .models import Sex
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def sex_view(request):
    sex_count = Sex.objects.filter(sex_user=request.user)

    form = SexForm()

    if request.method == 'POST':
        form = SexForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.sex_user = request.user
            form.save()

    context = {
        'sex_count': sex_count,
        'current_user': request.user
    }
    return render(request, 'sex/sex-counter.html', context)


def deleteSex(request, pk):
    sex = Sex.objects.get(id=pk)

    if request.method == 'POST':
        sex.delete()
        return redirect('/sex-counter')

    context = {
        'sex': sex
    }
    return render(request, 'sex/sex-counter.html', context)
