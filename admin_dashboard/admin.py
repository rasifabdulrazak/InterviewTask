from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ExamCategory)
admin.site.register(TypeOfExam)
admin.site.register(Questions)
admin.site.register(Answer)

