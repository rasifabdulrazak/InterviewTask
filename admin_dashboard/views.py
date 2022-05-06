from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def dashboard(request):
    category = ExamCategory.objects.all()
    form = Category()
    if request.method == 'POST':
        form = Category(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'category':category,
        'form':form,
    }
    return render(request,'admin_dashboard/index.html',context)

def delete_category(request,id):
   
    category = ExamCategory.objects.filter(pk=id)
    print(category)
    category.delete()
    return redirect('dashboard')