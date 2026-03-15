from django.shortcuts import render,redirect
from .models import ListItems

# Create your views here.
def home(request):
    listItems = ListItems.objects.all().order_by('-created_at')
    context = {
        'listItems': listItems
    }
    return render(request,'todo_app/home.html',context)


def addTask(request):
    task = request.GET.get('task')
    
    if task:
        ListItems.objects.create(title=task)
          
    return redirect('home')


def deleteTask(request,pk):
    task = ListItems.objects.get(id=pk)
        
    if task:
        task.delete()
    return redirect('home')


        