from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from core import serializers
# Create your views here.


# def add(request):   
#     t = TaskForm()
#     if request.method == 'POST':
#         t1 = TaskForm(request.POST)
#         if t1.is_valid():
#             t1.save()
#             return redirect('home')
#     context = {'task': t}
#     return render(request, 'form.html', context)


@api_view(['GET'])
def api(request):
    # obj = Task.objects.all()
    # context = {'obj': obj}
    # return render(request, 'home.html', context)
    api_urls = {
        'List': '/tasklist/',
        'Detail View': '/taskdetail/<str:pk>/',
        'created_at': '/taskcreate',
        'updated_at': '/taskupdate/<str:pk>/',
        'Delete': '/taskdelete/<str:pk>/'
    }
    return JsonResponse(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Deleted successfully')












