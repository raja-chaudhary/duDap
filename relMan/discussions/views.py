from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Discussion
from .forms import DiscussionForm
from django.contrib.auth.decorators import login_required
from lies.models import Lie
from dates.models import Date
from promises.models import Promise
from traits.models import Trait
# import chain method to chain multiple lists into one single list
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def discussion_view(request):

    discussions = Discussion.objects.filter(
        user=request.user).order_by('-updated')
    paginator = Paginator(discussions, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = DiscussionForm()

    if request.method == 'POST' and 'Create Discussion' in request.POST:
        form = DiscussionForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
        return redirect('/discussions')

    context = {'discussions': page_obj, 'form': form}

    return render(request, 'discussions/discussions.html', context)


@login_required
def updateDiscussion(request, pk):

    # discussion = Discussion.objects.get(id=pk)
    discussion = get_object_or_404(Discussion, id=pk, user=request.user)

    form = DiscussionForm(instance=discussion)

    if request.method == 'POST':
        form = DiscussionForm(request.POST, instance=discussion)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'discussion': discussion,
        'form': form
    }
    return render(request, 'discussions/update_discussion.html', context)


@login_required
def deleteDiscussion(request, pk):
    # discussion = Discussion.objects.get(id=pk)
    discussion = get_object_or_404(Discussion, id=pk, user=request.user)

    if request.method == 'POST':
        discussion.delete()
        return redirect('/')

    context = {
        'discussion': discussion
    }
    return render(request, 'discussions/delete.html', context)


def search(request):
    if request.method == 'GET':
        search_input = request.GET.get('search_input', False)
        searched_discussions = Discussion.objects.filter(
            content__contains=search_input)
        searched_lies = Lie.objects.filter(title__contains=search_input)
        searched_promises = Promise.objects.filter(
            content__contains=search_input)
        searched_dates = Date.objects.filter(title__contains=search_input)
        searched_traits_title = Trait.objects.filter(
            title__contains=search_input)
        searched_traits_content = Trait.objects.filter(
            content__contains=search_input)

        search_list = list(chain(searched_discussions, searched_lies,
                           searched_promises, searched_dates, searched_traits_title, searched_traits_content))
        return render(request, 'search.html', {'search_list': search_list})

    return render(request, 'search.html', {})
