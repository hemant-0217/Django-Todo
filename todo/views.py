from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todos
from .forms import TodoForm


def list(request):
    all = Todos.objects.order_by('id')
    form = TodoForm()

    return render(request, 'todo_page.html', {'todo_list': all, 'form': form})


@require_POST
def add(request):
    form = TodoForm(request.POST, request.FILES ) #doubt
    
    if form.is_valid():
        # new = Todos(name=request.POST['new_name'], img=request.POST['new_img'])
        name_add = form.cleaned_data.get("new_name")
        img_add = form.cleaned_data.get("new_img")
        new = Todos.objects.create(name=name_add, img=img_add)        
        new.save()

    return redirect('list')