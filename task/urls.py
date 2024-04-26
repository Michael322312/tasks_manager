from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TaskComplete,
    CommentDeleteView,
    CommentUpdateView,
    Register,
    CustomLoginView,
    CustomLogoutView,
    CommentLike
)


urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path("task_form/", TaskCreateView.as_view(), name="task_form"),
    path("<int:pk>/delete_task/", TaskDeleteView.as_view(), name="task_delete"),
    path("<int:pk>/update_task/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/complete", TaskComplete.as_view(), name="task_complete"),
    path("task/<int:pk>/comment_update", CommentUpdateView.as_view(), name="comment_update"),
    path("<int:pk>/delete_comment/", CommentDeleteView.as_view(), name="comment_delete"),
    path("log_in/", CustomLoginView.as_view(), name="log_in"),
    path("log_out/", CustomLogoutView.as_view(), name="log_out"),
    path("register/", Register.as_view(), name="register"),
    path("<int:pk>/like_comment", CommentLike.as_view(), name="comment_like")
]

app_name = "task"
