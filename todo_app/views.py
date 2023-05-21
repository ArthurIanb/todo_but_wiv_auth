from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Task

def home_page(req):
    """
        View for home page
    """
    context = {
        'tasks': Task.objects.all()
    }
    return render(req, 'home_page.html', context)


def new_task(req):
    """
        Create a new Task
    """
    if req.method == 'POST':
        title = req.POST.get('title')
        if req.user.id is None:
            return HttpResponseRedirect(reverse('login'))
        if title == '':
            return HttpResponseRedirect(reverse('home'))
        new_tank = Task(title=title, owner_id = req.user.id)
        new_tank.save()
    return HttpResponseRedirect(reverse('home'))


def change_state(req, pk):
    """
        Set done if not done or not done if done
    """
    if req.method == 'POST':
        if req.user.id is None:
            return HttpResponseRedirect(reverse('login'))
        obj = Task.objects.get(pk=pk)
        obj.done = not obj.done
        obj.save()
    return HttpResponseRedirect(reverse('home'))


def remove_task(req, pk):
    if req.method == 'POST':
        if req.user.id is None:
            return HttpResponseRedirect(reverse('login'))
        obj = Task.objects.get(pk=pk)
        obj.delete()
    return HttpResponseRedirect(reverse('home'))