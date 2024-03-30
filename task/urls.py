from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path("task_form/", TaskCreateView.as_view(), name="task_form")
]

