from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, StudySessionCreateView, StudySessionListView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('study_sessions/', StudySessionListView.as_view(), name='study-session-list'),
    path('study_sessions/create/', StudySessionCreateView.as_view(), name='study-session-create'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

]
