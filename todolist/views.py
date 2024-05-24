from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Todo

# Create your views here.

def index(request):
    all_todos = Todo.objects.all()
    context = dict(
        todos = all_todos
    )

    return render(request, 'todolist/index.html', context)

def add(request):
    new_todo = request.POST['todo']
    todo = Todo(text=new_todo)
    todo.save()

    return HttpResponseRedirect(reverse('todo-index'))

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.status = not todo.status
    todo.save()

    return HttpResponseRedirect(reverse('todo-index'))

def delete(request, todo_id):
    pass