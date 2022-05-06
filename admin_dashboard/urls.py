from django.urls import path,include
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete/<int:id>',views.delete_category,name ='delete')
]