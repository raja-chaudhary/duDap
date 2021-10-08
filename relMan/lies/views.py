from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lie
from .forms import LieForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def lie_view(request):

    lies = Lie.objects.filter(lie_user=request.user)

    form = LieForm()

    if request.method == 'POST':
        form = LieForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lie_user = request.user
            form.save()
        return redirect('/lies')

    context = {'lies': lies, 'form': form}

    return render(request, 'lies/lies.html', context)


def updateLie(request, pk):

    lie = Lie.objects.get(id=pk)

    form = LieForm(instance=lie)

    if request.method == 'POST':
        form = LieForm(request.POST, instance=lie)
        if form.is_valid():
            form.save()
            return redirect('/lies')

    context = {
        'lie': lie,
        'form': form
    }
    return render(request, 'lies/update_lie.html', context)


def deleteLie(request, pk):
    lie = Lie.objects.get(id=pk)

    if request.method == 'POST':
        lie.delete()
        return redirect('/lies')

    context = {
        'lie': lie
    }
    return render(request, 'lies/delete_lie.html', context)
