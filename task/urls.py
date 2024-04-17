from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path("task_form/", TaskCreateView.as_view(), name="task_form"),
    path("<int:pk>/delete_task/", TaskDeleteView.as_view(), name="task_delete"),
    path("<int:pk>/update_task/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/complete", TaskComplete.as_view(), name="task_complete"),
    path("task/<int:pk>/comment_update", CommentUpdateView.as_view(), name="comment_update"),
    path("<int:pk>/delete_comment/", CommentDeleteView.as_view(), name="comment_delete"),


]

