from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todolist_service.forms import TaskForm, TagForm
from todolist_service.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "todolist/index.html"


class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy("todolist_service:index")
    form_class = TaskForm
    template_name = "todolist/form.html"


class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy("todolist_service:index")
    form_class = TaskForm
    template_name = "todolist/form.html"


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todolist_service:index")
    template_name = "todolist/confirmation.html"


class TaskChangeStatusView(UpdateView):
    model = Task
    fields = []
    template_name = "todolist/form.html"
    success_url = reverse_lazy("todolist_service:index")

    def get_object(self, queryset=None):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        task = form.save(commit=False)
        task.is_done = not task.is_done
        task.save()
        return super().form_valid(form)


class TagListView(ListView):
    model = Tag
    template_name = "todolist/tags.html"


class TagCreateView(CreateView):
    model = Task
    success_url = reverse_lazy("todolist_service:tags")
    template_name = "todolist/form.html"
    form_class = TagForm


class TagUpdateView(UpdateView):
    model = Tag
    success_url = reverse_lazy("todolist_service:tags")
    template_name = "todolist/form.html"
    form_class = TagForm


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist_service:tags")
    template_name = "todolist/confirmation.html"
