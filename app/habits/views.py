from django.shortcuts import render
from .models import WeekOfHabit,GroupOfHabits


def table_of_week(request):
    context = {
        'habits': WeekOfHabit.objects.all(),
    }
    return render(request, 'table_of_week.html', context)


