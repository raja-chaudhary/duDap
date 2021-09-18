from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Discussion
from .forms import DiscussionForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def discussion_view(request):

    discussions = Discussion.objects.filter(user=request.user)

    form = DiscussionForm()

    if request.method == 'POST':
        form = DiscussionForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
        return redirect('/')

    context = {'discussions': discussions, 'form': form}

    return render(request, 'discussions/discussions.html', context)


def updateDiscussion(request, pk):

    discussion = Discussion.objects.get(id=pk)

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


def deleteDiscussion(request, pk):
    discussion = Discussion.objects.get(id=pk)

    if request.method == 'POST':
        discussion.delete()
        return redirect('/')

    context = {
        'discussion': discussion
    }
    return render(request, 'discussions/delete.html', context)


def test_func():
    return  # adding this function to check github push working or not
