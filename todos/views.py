from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date

# Create your views here.


class TodoListView(ListView):
    model = Todo

    def get_queryset(self):
        # Filter todos based on the user's session key
        session_key = self.request.session.session_key
        return Todo.objects.filter(session_key=session_key)


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        # Set the session key for the todo
        form.instance.session_key = self.request.session.session_key
        return super().form_valid(form)

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect("todo_list")
