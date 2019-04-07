from django.shortcuts import render

def to_do_list(request):
    return render(request, 'todolist/to_do_list.html', {})