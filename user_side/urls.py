from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.demo,name = 'demo'),
    path('exam_type/<int:pk>/',views.type_of_exam,name="type"),
    path('start_test/<int:id>/',views.start_test,name="start_test"),
]