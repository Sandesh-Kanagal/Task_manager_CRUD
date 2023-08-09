# tasks/views.py

# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Task
# import requests
import json
def tasklist(request):
    data=Task.objects.all()
    #  accessing individual data from task obj(named as data---line 9)
    content = {'tasks': data}
    # contents={'title':data['title'], 'description':data['description'], 'status':data['completed']}
    return render(request,'taskList.html', content)

def createTask(request):
    if request.method== "POST":
        data=request.POST

        taskTitle=data.get('title')
        taskDescription=data.get('description')
        taskCompleted = data.get('completed')
        
        if taskCompleted == 'on':
            taskCompleted = True
        else:
            taskCompleted = False

        Task.objects.create(
            title=taskTitle,
            description=taskDescription,
            completed = taskCompleted
        )

        return redirect("/api/tasks")
    
    return render(request, 'createTask.html')
def deleteTask(request, id):
    print(id)

    deleteQueryTask=Task.objects.get(id=id)
    deleteQueryTask.delete()

    return redirect("/api/tasks")

def updateTask(request,id):
    print(id)
    updateQueryTask=Task.objects.get(id=id)

    if request.method=="POST":
        data=request.POST

        TaskTitle=data.get('title')
        TaskDescription=data.get('description')
        taskCompleted = data.get('completed')

        if taskCompleted == 'on':
            taskCompleted = True
        else:
            taskCompleted = False

        updateQueryTask.title=TaskTitle
        updateQueryTask.description=TaskDescription
        updateQueryTask.completed=taskCompleted

        updateQueryTask.save()
        return redirect("/api/tasks")
    contents={'post':updateQueryTask}
    return render(request,'updateTask.html', contents)

