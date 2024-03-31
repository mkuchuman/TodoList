from django.urls import path

from todolist_service.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView, TaskChangeStatusView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/",
         TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/",
         TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/change_stat/",
         TaskChangeStatusView.as_view(),
         name="task-status-change"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tags-delete"),
]

app_name = "todolist_service"
