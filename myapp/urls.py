from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoList, name='todo'),
    path('newTask/', views.newTodo, name='newTodo'),
    path('doneTask/<id>/', views.doneTodo, name='doneTodo'),
    path('deleteTask/<id>/', views.deleteTodo, name='deleteTodo'),
]
