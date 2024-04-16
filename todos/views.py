from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date
import uuid

# Create your views here.


class TodoListView(ListView):
    model = Todo

    def get_queryset(self):
        # Get the unique identifier from the cookie
        user_identifier = self.request.COOKIES.get('user_identifier')

        # Check if there are todos for this user identifier
        if Todo.objects.filter(user_identifier=user_identifier).exists():
            # Return existing todos
            return Todo.objects.filter(user_identifier=user_identifier)
        else:
            # Create new todos for this user identifier
            # You can customize this part based on your requirements
            return Todo.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_identifier'] = self.request.COOKIES.get('user_identifier')
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if 'user_identifier' not in self.request.COOKIES:
            # Set a cookie for the user identifier if it doesn't exist
            user_identifier = generate_user_identifier()
            response.set_cookie('user_identifier', user_identifier)
        return response

def generate_user_identifier():
    return str(uuid.uuid4())


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

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
