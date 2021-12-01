from django.urls import path
from . import views


urlpatterns = [
    path('', views.table_of_week, name='table'),
    path('home/', views.home, name='home'),
    path('habit/', views.habit, name='habit'),
    path('habit-create/', views.HabitCreate.as_view(), name='habit-create'),
]