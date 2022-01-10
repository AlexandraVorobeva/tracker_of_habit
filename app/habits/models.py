from django.db import models
from django.contrib.auth.models import User



class GroupOfHabits(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    group = models.ForeignKey(GroupOfHabits, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WeekOfHabit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

    monday = models.BooleanField(default=False)
    monday_hours = models.FloatField(default=0, blank=True)

    tuesday = models.BooleanField(default=False)
    tuesday_hours = models.FloatField(default=0, blank=True)

    wednesday = models.BooleanField(default=False)
    wednesday_hours = models.FloatField(default=0, blank=True)

    thursday = models.BooleanField(default=False)
    thursday_hours = models.FloatField(default=0, blank=True)

    friday = models.BooleanField(default=False)
    friday_hours = models.FloatField(default=0, blank=True)

    saturday = models.BooleanField(default=False)
    saturday_hours = models.FloatField(default=0, blank=True)

    sunday = models.BooleanField(default=False)
    sunday_hours = models.FloatField(default=0, blank=True)


class Notes(models.Model):    #поменять на единственное число
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, )
    title = models.CharField(max_length=150, db_index=True, blank=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)


