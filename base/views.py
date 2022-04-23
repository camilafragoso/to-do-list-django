from asyncio import Task
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'tasklist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['tasklist'].filter(complete=False).count()
        return context

class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasklistlink')

class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasklistlink')

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'taskdetail'
    success_url = reverse_lazy('tasklistlink')
    #template_name = 'task_confirm_delete.html'
