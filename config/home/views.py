from django.shortcuts import render
from django.http import HttpResponse
from home.models import Todo

# Create your views here.


def introduction(request):
    return render(request, "index.html", {"name": "matin", "position": "ML Engineering", "age": 23})

def todo(request):
    all_todo = Todo.objects.all()
    return render(request, "todo.html", {"todo": all_todo})

def detail(request, todo_id):
    todo_item = Todo.objects.get(id=todo_id)
    return render(request, "detail.html", {"item": todo_item})
