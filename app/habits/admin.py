from django.contrib import admin
from .models import Habit, GroupOfHabits, WeekOfHabit


admin.site.register(Habit)
admin.site.register(GroupOfHabits)
admin.site.register(WeekOfHabit)
