from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add-task',views.addTask,name='add-task'),
    path('delete-task/<int:pk>/',views.deleteTask,name='delete-task')
]