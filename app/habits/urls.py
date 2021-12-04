from django.urls import path
from . import views


urlpatterns = [
    path('', views.table_of_week, name='table'),
    path('home/', views.home, name='home'),
    path('habit/', views.habit, name='habit'),
    path('habit-create/', views.HabitCreate.as_view(), name='habit-create'),
    path('habit-delete/<int:pk>/', views.HabitDelete.as_view(), name='habit-delete'),
    path('week-habit-create/', views.WeekOfHabitCreate.as_view(), name='week-habit-create'),
]