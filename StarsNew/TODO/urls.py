from django.urls import path
from .views import ContactCreate
from . import views



urlpatterns = [
    # ToDoList URLs
    path('', views.todolist_list, name='todolist_list'),
    path('todolists/', views.todolist_list, name='todolist_list'),
    path('todolist/<int:pk>/', views.todolist_detail, name='todolist_detail'),
    path('todolist/new/', views.todolist_create, name='todolist_create'),
    path('todolist/<int:pk>/edit/', views.todolist_update, name='todolist_update'),
    path('todolist/<int:pk>/delete/', views.todolist_delete, name='todolist_delete'),
     path('contact', ContactCreate.as_view(),name='contact'),

    # Task URLs
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:pk>/list/', views.task_list_bytodolist, name='task_list_bytodolist'),
    path('task/<int:pk>/edittodo/', views.todolist_update, name='task_list_updatebytodo'),
    path('task/<int:pk>/deletetodo/', views.todolist_delete, name='task_list_deltebytodo'),
    path('task/<int:pk>/bycompleted/', views.task_list_bycompleted, name='task_list_bytodocompleted'),
    path('task/<int:pk>/bypending/', views.task_list_bypending, name='task_list_bytodopending'),
    path('task/<int:pk>/inprogress/', views.task_list_byinprogress, name='task_list_bytodoinprogress'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
