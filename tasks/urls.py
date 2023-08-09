# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasklist, name='task-list'),
    path('createTask/', views.createTask, name='create-task'),
    path('deleteTask/<id>/', views.deleteTask, name='delete-task'),
    path('updateTask/<id>/', views.updateTask, name='update-task')

    # path('tasks/<int:task_id>/', views.task_detail, name='task-detail'),
]
