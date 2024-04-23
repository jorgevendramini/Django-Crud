from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url="/loginPage/login_user/"), name="dispatch")
class TodoListView(LoginRequiredMixin, ListView):
    model = Todo

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y"), input_formats=["%d%m%Y", "%d/%m/%Y"]
    )

    class Meta:
        model = Todo
        fields = ["title", "deadline"]


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect("todo_list")
