from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from django import forms

# Create your views here.


class TodoListView(ListView):
    model = Todo


class TodoForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y"), input_formats=["%d%m%Y", "%d/%m/%Y"]
    )

    class Meta:
        model = Todo
        fields = ["title", "deadline"]


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
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
