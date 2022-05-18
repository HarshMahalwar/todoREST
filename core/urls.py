from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.api, name='api'),
    # path('add', views.add, name='add'),
    path('tasklist', views.taskList, name='taskList'),
    path('taskdetail/<str:pk>/', views.taskDetail, name='taskDetail'),
    path('taskcreate', views.taskCreate, name='taskCreate'),
    path('taskupdate/<str:pk>', views.taskUpdate, name='taskUpdate'),
    path('taskdelete/<str:pk>', views.taskDelete, name='taskDelete')
]