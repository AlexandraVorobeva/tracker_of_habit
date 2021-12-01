from django.shortcuts import render
from .models import WeekOfHabit, GroupOfHabits, Habit
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home.html')


def table_of_week(request):
    context = {
        'habits': WeekOfHabit.objects.all(),
    }
    return render(request, 'table_of_week.html', context)


def habit(request):
    context = {
        'groups': GroupOfHabits.objects.all(),
        'habits': Habit.objects.all(),
    }
    return render(request, 'habit.html', context)


class HabitCreate(CreateView):
    model = Habit
    fields = ['name', 'group']
    success_url = reverse_lazy('habit')


class HabitDelete(DeleteView):
    model = Habit
    context_object_name = 'habit'
    success_url = reverse_lazy('habit')


