from django.db.models.query import QuerySet
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DeleteView,
    UpdateView
)
from django.shortcuts import redirect, get_object_or_404
from task.models import Comment, Task
from task.forms import CommentForm, TaskFilterForm, TaskCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from task.mixins import UserIsOwnerMixin
from django.core.exceptions import ValidationError, PermissionDenied
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Count


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task/task_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status', '')
        task_for = self.request.GET.get('task_for', '')

        if status:
            queryset = queryset.filter(status=status)
        if task_for == "MY_TASKS":
            queryset = queryset.filter(task_for=self.request.user)
        elif task_for == "CREATED_BY_ME":
            queryset = queryset.filter(creator=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)
        return context


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context:
            context["form"] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)
        if not self.request.user.is_authenticated:
            messages.add_message(
                request,
                messages.INFO,
                "Unauthenicaded users can't write comments"
            )
            referring_url = request.META.get('HTTP_REFERER')
            return redirect(referring_url)
        elif form.is_valid():
            comment = form.save(commit=False)
            comment.creator = request.user
            comment.task = self.get_object()
            comment.save()
            return redirect("task:task_detail", pk=comment.task.pk)
        else:
            raise ValidationError(message="Bad input")


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy("task:task_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    template_name = "task/delete_confirm.html"
    success_url = reverse_lazy("task:task_list")


class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    template_name = "task/update_task.html"
    success_url = reverse_lazy("task:task_list")
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
        return HttpResponseRedirect((reverse_lazy("task:task_list")))


class CommentLike(LoginRequiredMixin, UpdateView):
    model = Comment

    def get_object(self):
        comment_id = self.kwargs.get("pk")
        return get_object_or_404(Comment, pk=comment_id)

    def post(self, request, *args, **kwargs):
        comment = self.get_object()
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
        comment.save()
        return HttpResponseRedirect((reverse_lazy("task:task_detail", kwargs={'pk': self.get_object().task.id})))


class CommentUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comment/creation_form.html"

    def form_valid(self, form):
        comment = self.get_object()
        if comment.creator == self.request.user:
            return super().form_valid(form)
        raise PermissionDenied("You did not wrote this comment")

    def get_success_url(self):
        return reverse_lazy("task:task_detail", kwargs={'pk': self.object.task.id})


class CommentDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Comment
    template_name = "comment/delete_form.html"

    def get_success_url(self):
        return reverse_lazy("task:task_detail", kwargs={'pk': self.object.task.id})


class CustomLoginView(LoginView):
    template_name = "auth/log_in.html"
    redirect_authenticated_user = "task_list"


class CustomLogoutView(LogoutView):
    next_page = "task:log_in"


class Register(CreateView):
    template_name = "auth/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("log_in")
