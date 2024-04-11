from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, View
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .mixins import *
# Create your views here.


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name="task/task_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status', '')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)
        return context


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name="task/task_detail.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name="task/task_form.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    template_name = "task/delete_confirm.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    template_name = "task/update_task.html"
    success_url = reverse_lazy("task_list")
    form_class = TaskCreateForm


class TaskComplete(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    def get_object(self):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(Task, pk=task_id)
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = 'DONE'
        task.save()
        return HttpResponseRedirect((reverse_lazy("task_list")))