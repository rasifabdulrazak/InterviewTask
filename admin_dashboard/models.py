from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExamCategory(models.Model):
    name = models.CharField(max_length=300)
    added_date = models.DateTimeField(auto_now_add=True,null=True)
    title = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class TypeOfExam(models.Model):
    category = models.ForeignKey(ExamCategory,on_delete=models.CASCADE,related_name= 'exam_type') 
    name = models.CharField(max_length=300)
    added_date = models.DateTimeField(auto_now_add=True,null=True)
    no_of_questions = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Questions(models.Model):
    type_of_exam = models.ForeignKey(ExamCategory,on_delete=models.CASCADE,related_name= 'questions')  
    added_date = models.DateTimeField(auto_now_add=True,null=True)
    question_number = models.IntegerField()
    question = models.TextField()

    def __str__(self):
        return self.question

class Answer(models.Model):
    question =  models.ForeignKey(Questions,on_delete=models.CASCADE,related_name= 'answer') 
    answer = models.CharField(max_length=300)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

