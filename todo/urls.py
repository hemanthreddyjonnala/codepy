from django.urls import path
from .views import todoView, addTodo, deleteOrUpdateTodo

urlpatterns = [
    path('', todoView, name='todo' ),
    path('addTodo/', addTodo, name='todo-add-item' ),
    path('deleteOrUpdateTodo/<int:todo_id>/', deleteOrUpdateTodo, name='todo-delete-update-item' ),

]
