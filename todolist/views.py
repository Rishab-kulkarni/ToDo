from django.shortcuts import render, redirect
from .forms import CreateNewList
from .models import TODOList

from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    items = TODOList.objects.all().order_by('-addedDate')
    
    print(items)
    return render(request, 'todolist/home.html', {
        "items" : items
    })


def add(request):
    # print(request.POST)
    text = request.POST['content']
    current_date = timezone.now()
    
    TODOList.objects.create(addedDate = current_date, text = text)

    return HttpResponseRedirect('/')


@csrf_exempt
def delete(request, todo_id):
    print(todo_id)
    TODOList.objects.filter(id = todo_id).delete()
    return HttpResponseRedirect('/')
    