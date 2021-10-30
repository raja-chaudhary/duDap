from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trait
from .forms import TraitForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.


@login_required
def traits_view(request):
    traits = Trait.objects.filter(trait_user=request.user)
    paginator = Paginator(traits, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = TraitForm()

    if request.method == 'POST':
        form = TraitForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.trait_user = request.user
            form.save()
        return redirect('/traits')

    context = {'traits': page_obj, 'form': form}

    return render(request, 'traits/traits.html', context)


@login_required
def updateTrait(request, pk):

    trait = Trait.objects.get(id=pk)

    form = TraitForm(instance=trait)

    if request.method == 'POST':
        form = TraitForm(request.POST, instance=trait)
        if form.is_valid():
            form.save()
            return redirect('/traits')

    context = {
        'trait': trait,
        'form': form
    }
    return render(request, 'traits/update_trait.html', context)


@login_required
def deleteTrait(request, pk):
    trait = Trait.objects.get(id=pk)

    if request.method == 'POST':
        trait.delete()
        return redirect('/traits')

    context = {
        'trait': trait
    }
    return render(request, 'traits/delete_trait.html', context)
