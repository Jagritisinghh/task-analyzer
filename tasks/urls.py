from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list_create, name='task-list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task-detail'),
]