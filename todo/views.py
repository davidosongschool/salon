from django.shortcuts import render
from .models import Item #Use item models in views.py

# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo.html', context)
