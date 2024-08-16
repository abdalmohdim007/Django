from django.db import models

class EA(models.Model):
  BA = models.CharField(max_length=255)
  AA = models.CharField(max_length=255)
  DA = models.CharField(max_length=255, null=True)
  TA = models.CharField(max_length=255, null=True)

def __str__(self):
    return f"{self.BA} {self.AA}"
