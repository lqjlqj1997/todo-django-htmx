from django.shortcuts import render
from django.http import HttpResponse
from . import models


def todoList(request):
    todoList = models.Todo.objects.all()
    return render(request, "home.html", {'todoList':  todoList})


# Create your views here.
def newTodo(request):
    body = request.body.decode('utf-8')
    req_dict = {}
    for data in body.split("&"):
        print(data )
        key, value = data.split("=")
        req_dict[key] = value

    todoList = list(models.Todo.objects.all().order_by('id'))
    try :
        newId = todoList[-1].id + 1
    except  : 
        newId = 0
    # newTask = {}
    models.Todo.objects.create(id= newId, name = req_dict["task"] ,  completed= False )
    todoList = models.Todo.objects.all().order_by('id')

    if request.htmx:
        template_name = "todoList.html"
    else:
        template_name = "home.html"

    return render(request, template_name, {'todoList':  todoList})

def doneTodo(request, id):
    print(f"{id=}")
    
    todo = models.Todo.objects.get(id=id)
    todo.completed = True
    todo.save()

    return render(request, "todo.html", {'i':  todo})

def deleteTodo(request, id):
    print(f"{id=}")
    
    todo = models.Todo.objects.get(id=id)
    todo.delete()

    return HttpResponse("")
    