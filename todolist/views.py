from django.shortcuts import render
from .models import TodoList

def to_do_list(request):

	todos = TodoList.objects.all() #quering all todos with the object manager
	return render(request, 'todolist/to_do_list.html', {"todos": todos})



