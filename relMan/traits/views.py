from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trait
from .forms import TraitForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def traits_view(request):
    traits = Trait.objects.filter(trait_user=request.user)
    print(traits)

    form = TraitForm()

    if request.method == 'POST':
        form = TraitForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.trait_user = request.user
            form.save()
        return redirect('/traits')

    context = {'traits': traits, 'form': form}

    return render(request, 'traits/traits.html', context)
