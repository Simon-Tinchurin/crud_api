from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name=''),
    path('create/', views.create, name='create'),
    path('completed-tasks/', views.completed, name='completed'),
    path('tasks-in-progress/', views.in_progress, name='in_progress'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('edit/<int:task_id>/', views.edit, name='edit'),
    path('done/<int:task_id>/', views.done, name='done'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
]


