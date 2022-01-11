from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('table/', views.TableOfWeek.as_view(), name='table'),
    path('habit/', views.Habits.as_view(), name='habit'),
    path('contact/', views.contact, name='contact'),
    path('notes/', views.Notess.as_view(), name='notes'),

    path('habit-create/', views.HabitCreate.as_view(), name='habit-create'),
    path('habit-delete/<int:pk>/', views.HabitDelete.as_view(), name='habit-delete'),

    path('week-habit-create/', views.WeekOfHabitCreate.as_view(), name='week-habit-create'),
    path('week-habit-update/<int:pk>/', views.WeekOfHabitUpdate.as_view(), name='week-habit-update'),
    path('week-habit-delete/<int:pk>/', views.WeekHabitDelete.as_view(), name='week-habit-delete'),

    path('group-delete/<int:pk>/', views.GroupOfHabitDelete.as_view(), name='group-delete'),
    path('group-create/', views.GroupOfHabitCreate.as_view(), name='group-create'),

    path('note-create/', views.NotesCreate.as_view(), name='note-create'),
    path('note-delete/<int:pk>/', views.NotesDelete.as_view(), name='note-delete'),


]