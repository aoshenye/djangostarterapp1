from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    return render(request, 'todo1/todo_list.html')
