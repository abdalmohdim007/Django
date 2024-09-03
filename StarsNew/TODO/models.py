from django.db import models
from django.contrib.auth.models import User

# ToDoList Model
class ToDoList(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Task Model
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    CATEGORY_CHOICES = [
        ('fun', 'Fun'),
        ('business', 'Business'),
        ('personal', 'Personal'),
        ('tech', 'Technology'),
    ]
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Teaching')
    file = models.FileField(upload_to='uploads/', null=True, blank=True)  # New field for file upload
    
    def __str__(self):
        return self.name

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
