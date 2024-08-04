from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Task, StudySession
from .forms import TaskForm, StudySessionForm
from django.utils import timezone


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tracker/task_list.html'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tracker/task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tracker/task_form.html'
    success_url = reverse_lazy('task-list')
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tracker/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')  # Redirect to task list or another appropriate URL
    template_name = 'tracker/task_confirm_delete.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
class StudySessionListView(ListView):
    model = StudySession
    template_name = 'tracker/study_session_list.html'
    context_object_name = 'study_sessions'

class StudySessionListView(ListView):
    model = StudySession
    template_name = 'tracker/study_session_list.html'
    context_object_name = 'study_sessions'

class StudySessionCreateView(CreateView):
    model = StudySession
    form_class = StudySessionForm
    template_name = 'tracker/study_session_form.html'
    
    def form_valid(self, form):
        study_session = form.save(commit=False)
        study_session.user = self.request.user
        study_session.start_time = timezone.now()
        duration = form.cleaned_data['duration']
        study_session.end_time = study_session.start_time + timezone.timedelta(minutes=duration)
        study_session.save()
        return redirect('study-session-list')
    
class HomeView(TemplateView):
    template_name = 'tracker/home.html'