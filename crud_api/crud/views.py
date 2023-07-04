from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm


# list of tasks
def tasks(request):
    if request.method == "GET":
        all_tasks = Task.objects.all().order_by('-created_at')
        return render(request, 'user_page.html', {'tasks': all_tasks})
    else:
        return HttpResponseNotAllowed(['GET'])


# single task
def task(request, task_id):
    if request.method == "GET":
        single_task = get_object_or_404(Task, id=task_id)
        return render(request, 'task.html', {'task': single_task})
    else:
        return HttpResponseNotAllowed(['GET'])


# completed tasks
def completed(request):
    if request.method == "GET":
        tasks = Task.objects.filter(completed=True)
        return render(request, 'completed.html', {'tasks': tasks})
    else:
        return HttpResponseNotAllowed(['GET'])


# tasks in progress
def in_progress(request):
    if request.method == "GET":
        tasks = Task.objects.filter(completed=False)
        return render(request, 'in_progress.html', {'tasks': tasks})
    else:
        return HttpResponseNotAllowed(['GET'])


# create task
def create(request):
        form = TaskForm()
        context = {'form': form}
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save()
                task.save()
                return redirect('')
        elif request.method == 'GET':
            return render(request, 'create.html', context)
        else:
            return HttpResponseNotAllowed(['GET', 'POST'])


# edit task
def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('')
    elif request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'edit.html', {'form': form})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


# complete task
def done(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, id=task_id)
        task.completed = True
        task.save()
        return redirect('')
    else:
        return HttpResponseNotAllowed(['GET'])


# delete task
def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('')