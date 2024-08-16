from django.db import models

# Create your models here.


class companydb(models.Model):
  company = models.CharField(max_length=255)
  department = models.CharField(max_length=255)
  employeeID = models.CharField(max_length=255)
  employee_lastname = models.CharField(max_length=255)
  employee_firstname = models.CharField(max_length=255)
  birthdate = models.CharField(max_length=255)
  vacations = models.CharField(max_length=255)
  used_vacations = models.CharField(max_length=255)
  salary = models.CharField(max_length=255,null=True)

  def __str__(self):
    return f"{self.employeeID} {self.employee_firstname}"