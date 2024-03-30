from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .models import *

from .forms import *
from django.urls import reverse_lazy

# Create your views here.


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name="task/task_list.html"

class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name="task/task_detail.html"

class TaskCreateView(CreateView):
    model = Task
    template_name="task/task_form.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_list")