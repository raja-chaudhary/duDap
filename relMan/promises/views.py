from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Promise
from .forms import PromiseForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def promise_view(request):

    promises = Promise.objects.filter(promise_user=request.user)

    form_promise = PromiseForm()

    if request.method == 'POST':
        form_promise = PromiseForm(request.POST or None)
        if form_promise.is_valid():
            instance = form_promise.save(commit=False)
            instance.promise_user = request.user
            form_promise.save()
        return redirect('/promises')

    context = {'promises': promises, 'form': form_promise}

    return render(request, 'promises/promises.html', context)


def updatePromise(request, pk):

    promise = Promise.objects.get(id=pk)

    form = PromiseForm(instance=promise)

    if request.method == 'POST':
        form = PromiseForm(request.POST, instance=promise)
        if form.is_valid():
            form.save()
            return redirect('/promises')

    context = {
        'promise': promise,
        'form': form
    }
    return render(request, 'promises/update_promise.html', context)


def deletePromise(request, pk):
    promise = Promise.objects.get(id=pk)

    if request.method == 'POST':
        promise.delete()
        return redirect('/promises')

    context = {
        'promise': promise
    }
    return render(request, 'promises/delete_promise.html', context)
