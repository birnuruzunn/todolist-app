from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoList

def to_do_list(request):

	todos = TodoList.objects.order_by('id') #quering all todos with the object manager
	"""
	if request.method == "POST": #checking if the request method is a POST
		if "save" in request.POST: #checking if there is a request to add a todo
			title = request.POST["description"] #title
			date = str(request.POST["date"]) #date
			
			content = title + " -- " + date + " " 
			new_list = TodoList(title=title, due_date=date)
			new_list.save() #saving the todo 
			return redirect("/") #reloading the page

		if "taskCompleted" in request.POST:
			completed =TodoList.objects.get('id')
			completed.complete = True
			completed.save()

		if "taskDelete" in request.POST: #checking if there is a request to delete a todo
			delete_list = TodoList.objects.get('id') #getting todo id
			delete_list.delete() #deleting todo
	"""
	return render(request, 'todolist/to_do_list.html', {"todos": todos})

def addTodo(request):
	title = request.POST["title"] #title
	date = str(request.POST["date"]) #date
	content = title + " -- " + date + " " 

	new_list = TodoList(title=title,  content=content, due_date=date)
	new_list.save() #saving the todo
	return HttpResponseRedirect('/')
def deleteTodo(request, todo_id):
	delete_list = TodoList.objects.get(id=todo_id) #getting todo id
	delete_list.delete() #deleting todo
	return HttpResponseRedirect('/')