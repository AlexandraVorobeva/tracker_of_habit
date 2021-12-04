from django.urls import path
from . import views


urlpatterns = [
    path('table/', views.table_of_week, name='table'),
    path('', views.home, name='home'),
    path('habit/', views.habit, name='habit'),
    path('habit-create/', views.HabitCreate.as_view(), name='habit-create'),
    path('habit-delete/<int:pk>/', views.HabitDelete.as_view(), name='habit-delete'),
    path('week-habit-create/', views.WeekOfHabitCreate.as_view(), name='week-habit-create'),
    path('group-delete/<int:pk>/', views.GroupOfHabitDelete.as_view(), name='group-delete'),
    path('group-create/', views.GroupOfHabitCreate.as_view(), name='group-create'),
]