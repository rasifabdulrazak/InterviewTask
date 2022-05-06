from django import forms
from .models import *

class Category(forms.ModelForm):
    class Meta:
        model = ExamCategory
        fields = '__all__'