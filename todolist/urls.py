from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('create/', views.create, name="create"),
    # path('view/', views.view, name="view"),
    path('add/',views.add, name="add"),
    path('delete/<int:todo_id>/', views.delete, name="delete"),
]