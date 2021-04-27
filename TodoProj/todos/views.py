from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Todo

# Create your views here.
def list_todo_items(request):
    # To display our enter data
    # this is to list all the todo in to the templates
    context = {'todo_list': Todo.objects.all()}
    return render(request,'todos/todo_list.html',context)

# this is accept input
def insert_todo_item(request:HttpRequest):
    # this is to link the app to the database and 'content' is the placeholder name in the html
    todo = Todo(content = request.POST['content'])    #i created an obj for the model and link it to the html 
    # this is use to save the model
    todo.save()
    return redirect('/todos/list/')

def delete_todo_item(request,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')