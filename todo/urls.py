from django.urls import path
from .views import TaskListView,TaskCreateView,TaskUpdateView,Home,DeleteTask


urlpatterns = [
    path('', Home,name="home"),
    path('list/<str:username>', TaskListView.as_view(),name="todo-home"),
    path('create/', TaskCreateView.as_view(),name="todo-create"),
    path('update/<int:pk>', TaskUpdateView.as_view(),name="todo-update"),
    path('delete/<int:id>', DeleteTask,name="todo-delete"),
]
