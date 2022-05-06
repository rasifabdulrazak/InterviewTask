from django.shortcuts import render
from admin_dashboard.models import *

# Create your views here.


def demo(request):
    category = ExamCategory.objects.all()
    context = {
        'category':category,
    }
    return render(request,'user_side/index.html',context)

def type_of_exam(request,pk):
    exam_type = TypeOfExam.objects.filter(category=pk)
    context = {
        'exam_type':exam_type,
    }
    return render(request,'user_side/exam.html',context)

def start_test(request,id):
    exam_type = TypeOfExam.objects.get(id=id)
    pk = ExamCategory.objects.get(id=exam_type.category.id)
    print(pk)
    dic ={}
    questions = Questions.objects.filter(type_of_exam = pk)
    for i in questions:

        answers = Answer.objects.filter(question=i)
        dic[i] = answers
    print(dic)
    
    print(questions)
    answers = Answer.objects.filter(question__in=questions)
    print(answers)
    context = {
        'questions':questions,
        'answers':answers,
        
    }
    return render(request,'user_side/start.html',context,{'dic':dic})