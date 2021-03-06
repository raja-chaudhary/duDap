from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lie
from .forms import LieForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def lie_view(request):

    lies = Lie.objects.filter(lie_user=request.user).order_by('-updated')
    print(lies)
    paginator = Paginator(lies, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = LieForm()

    if request.method == 'POST':
        form = LieForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lie_user = request.user
            form.save()
        return redirect('/lies')

    context = {'lies': page_obj, 'form': form}

    return render(request, 'lies/lies.html', context)


@login_required
def updateLie(request, pk):

    # lie = Lie.objects.get(id=pk)
    lie = get_object_or_404(Lie, id=pk, lie_user=request.user)

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


@login_required
def deleteLie(request, pk):
    # lie = Lie.objects.get(id=pk)
    lie = get_object_or_404(Lie, id=pk, lie_user=request.user)

    if request.method == 'POST':
        lie.delete()
        return redirect('/lies')

    context = {
        'lie': lie
    }
    return render(request, 'lies/delete_lie.html', context)
