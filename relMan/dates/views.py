from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Date, REMINDER_CHOICES
from .forms import DateForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def date_view(request):

    dates = Date.objects.filter(date_user=request.user)
    paginator = Paginator(dates, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = DateForm()

    if request.method == 'POST':
        form = DateForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.date_user = request.user
            form.save()
        return redirect('/dates')

    context = {'dates': page_obj, 'form': form,
               'reminder_choices': REMINDER_CHOICES}

    return render(request, 'dates/dates.html', context)


def updateDate(request, pk):

    date = Date.objects.get(id=pk)

    form = DateForm(instance=date)

    if request.method == 'POST':
        form = DateForm(request.POST, instance=date)
        if form.is_valid():
            form.save()
            return redirect('/dates')

    context = {
        'date': date,
        'form': form
    }
    return render(request, 'dates/update_date.html', context)


def deleteDate(request, pk):
    date = Date.objects.get(id=pk)

    if request.method == 'POST':
        date.delete()
        return redirect('/dates')

    context = {
        'date': date
    }
    return render(request, 'dates/delete_date.html', context)
