from django.contrib import admin
from .models import Habit, GroupOfHabits, WeekOfHabit, Notes


admin.site.register(Habit)
admin.site.register(GroupOfHabits)
admin.site.register(WeekOfHabit)
admin.site.register(Notes)
