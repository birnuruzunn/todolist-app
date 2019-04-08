from django.shortcuts import render
from .models import TodoList

def to_do_list(request):

	todos = TodoList.objects.all() #quering all todos with the object manager
	

	if request.method == "POST": #checking if the request method is a POST
		if "save" in request.POST: #checking if there is a request to add a todo
			title = request.POST["description"] #title
			date = str(request.POST["date"]) #date
			
			content = title + " -- " + date + " " 
			Todo = TodoList(title=title, due_date=dates)
			Todo.save() #saving the todo 
			return redirect("/") #reloading the page
		if "taskDelete" in request.POST: #checking if there is a request to delete a todo
			todo = TodoList.objects.get(id) #getting todo id
			todo.delete() #deleting todo

	return render(request, 'todolist/to_do_list.html', {"todos": todos})



