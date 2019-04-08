from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoList

def to_do_list(request):
	todos = TodoList.objects.order_by('id') #quering all todos with the object manager
	return render(request, 'todolist/to_do_list.html', {"todos": todos})

def addTodo(request):
	title = request.POST["title"] #title
	date = str(request.POST["date"]) #date
	content = title + " -- " + date + " " 

	new_list = TodoList(title=title,  content=content, due_date=date)
	new_list.save() #saving the todo	
	return HttpResponseRedirect('/')

def completeTodo(request,todo_id):
	complete_list = TodoList.objects.get(id=todo_id) #getting todo id
	complete_list.completed = True
	complete_list.save()
	return HttpResponseRedirect('/')

def uncompleteTodo(request,todo_id):
	complete_list = TodoList.objects.get(id=todo_id) #getting todo id
	complete_list.completed = False
	complete_list.save()
	return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
	delete_list = TodoList.objects.get(id=todo_id) #getting todo id
	delete_list.delete() #deleting todo
	return HttpResponseRedirect('/')