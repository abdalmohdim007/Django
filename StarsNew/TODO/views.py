from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from .models import Task, ToDoList, Contact
from .forms import TaskForm, ToDoListForm, ContactForm
from django.views.generic.edit import CreateView




# List all to-do lists
@login_required
def todolist_list(request):
    
    todolists = ToDoList.objects.filter(user=request.user)
    return render(request, 'TODO/todolist_list.html', {'todolists': todolists})

# List all to-do lists
@login_required
def test_session(request):
    currentpage = request.session.get('cuurentpage', "i am on todolist page")
    
    request.session['currentpage'] = currentpage
    print('my page is', currentpage)
    todolists = ToDoList.objects.filter(user=request.user)
    return render(request, 'TODO/todolist_list.html', {'todolists': todolists})




# View a specific to-do list
@login_required
def todolist_detail(request, pk):
    
    todolist = get_object_or_404(ToDoList, pk=pk, user=request.user)
    return render(request, 'TODO/todolist_detail.html', {'todolist': todolist})

# Create a new to-do list
@login_required
def todolist_create(request):
    print('this was the previous page',request.session['currentpage'] )
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            todolist = form.save(commit=False)
            todolist.user = request.user
            todolist.save()
            form.save_m2m()  # Save the many-to-many data
            return redirect('todolist_list')
    else:
        form = ToDoListForm()
    return render(request, 'TODO/todolist_form.html', {'form': form})

# Update an existing to-do list
@login_required
def todolist_update(request, pk):
    todolist = get_object_or_404(ToDoList, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ToDoListForm(request.POST, instance=todolist)
        if form.is_valid():
            form.save()
            return redirect('todolist_detail', pk=todolist.pk)
    else:
        form = ToDoListForm(instance=todolist)
    return render(request, 'TODO/todolist_form.html', {'form': form})

# Delete a to-do list
@login_required
def todolist_delete(request, pk):
    todolist = get_object_or_404(ToDoList, pk=pk, user=request.user)
    if request.method == 'POST':
        todolist.delete()
        return redirect('todolist_list')
    return render(request, 'TODO/todolist_confirm_delete.html', {'todolist': todolist})

# List all tasks
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'TODO/task_list.html', {'tasks': tasks})

#Get tasks by todo list
@login_required
def task_list_bytodolist(request, pk):
    todolist = get_object_or_404(ToDoList, id=pk)
    tasks = Task.objects.filter(user=request.user,todolist=todolist)
    return render(request, 'TODO/task_list.html', {'tasks': tasks})

#Get tasks by todo list and status completed
@login_required
def task_list_bycompleted(request, pk):
    todolist = get_object_or_404(ToDoList, id=pk)
    tasks = Task.objects.filter(user=request.user,todolist=todolist,status='completed')
    return render(request, 'TODO/task_list.html', {'tasks': tasks})

@login_required
def task_list_bypending(request, pk):
    todolist = get_object_or_404(ToDoList, id=pk)
    tasks = Task.objects.filter(user=request.user,todolist=todolist,status='pending')
    return render(request, 'TODO/task_list.html', {'tasks': tasks})


@login_required
def task_list_byinprogress(request, pk):
    todolist = get_object_or_404(ToDoList, id=pk)
    tasks = Task.objects.filter(user=request.user,todolist=todolist,status='in_progress')
    return render(request, 'TODO/task_list.html', {'tasks': tasks})


# View a specific task
@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'TODO/task_detail.html', {'task': task})

# Create a new task
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'TODO/task_form.html', {'form': form})

# Update an existing task
@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'TODO/task_form.html', {'form': form})

# Delete a task
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'TODO/task_confirm_delete.html', {'task': task})

class ContactCreate(CreateView):
 
    # specify the model for list view
    model = Contact
    form_class = ContactForm
    success_url = "studentlist"


    