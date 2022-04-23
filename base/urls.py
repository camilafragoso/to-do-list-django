from django.urls import path
from .views import CreateTask, DeleteTask, TaskList, UpdateTask

urlpatterns = [
    path('', TaskList.as_view(), name='tasklistlink'),
    path('create', CreateTask.as_view(), name='createtasklink'),
    path('update/<int:pk>/', UpdateTask.as_view(), name='updatetasklink'),
    path('delete/<int:pk>/', DeleteTask.as_view(), name='deletetasklink'),


]