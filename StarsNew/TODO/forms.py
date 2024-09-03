from django import forms
from .models import Task, ToDoList, Contact

# Form for the Task model
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','todolist', 'start_date', 'finish_date', 'due_date', 'description', 'status', 'category', 'file']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'finish_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
# Form for the ToDoList model
class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name', 'description']
       # widgets = {
       #     'tasks': forms.CheckboxSelectMultiple(),  # Makes the task selection easier to manage
       # }
    def __init__(self, *args, **kwargs):
        super(ToDoListForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
    

        fields = ['name', 'email', 'message',]
    
   # This formats the fields, but make sure you add the template tags
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            