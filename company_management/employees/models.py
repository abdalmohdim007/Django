from django.db import models
from hr.models import Employee

class Profile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.TextField()
    certifications = models.TextField()

    def __str__(self):
        return f"{self.employee.user.first_name} {self.employee.user.last_name}"

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    comments = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.employee.user.first_name} {self.employee.user.last_name} - {self.review_date}"
