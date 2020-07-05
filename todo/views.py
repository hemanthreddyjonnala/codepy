from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TodoItem


# Create your views here.
@login_required
def todoView(request):
    context = {'todos':TodoItem.objects.all()}
    return render(request, 'todo/todo.html', context)


def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteOrUpdateTodo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)

    if request.POST.get("Delete"):
        item.delete()
    elif request.POST.get("Update"):
        TodoItem.objects.filter(pk=todo_id).update(content=request.POST["todo_text_content"])
    return HttpResponseRedirect('/todo/')







