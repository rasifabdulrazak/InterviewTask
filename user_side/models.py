from django.db import models
from admin_dashboard.models import *

class Student(models.Model):
    std_id = models.CharField(max_length=10)
    exam = models.ForeignKey(TypeOfExam, on_delete=models.CASCADE,related_name='student')
    score = models.PositiveIntegerField()


