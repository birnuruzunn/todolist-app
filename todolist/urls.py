from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_do_list, name='to_do_list'),
    path('addTodo/', views.addTodo, name='addTodo'),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name='deleteTodo'),
    path('completeTodo/<int:todo_id>/', views.completeTodo, name='completeTodo'),
    path('uncompleteTodo/<int:todo_id>/', views.uncompleteTodo, name='uncompleteTodo'),
]