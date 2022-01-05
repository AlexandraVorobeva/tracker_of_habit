from django.shortcuts import render
from .models import WeekOfHabit, GroupOfHabits, Habit
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models import Sum


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


class TableOfWeek(LoginRequiredMixin, ListView):
    model = Habit
    template_name = 'table_of_week.html'
    context_object_name = 'base_habits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habits'] = WeekOfHabit.objects.all()
        context['habits'] = context['habits'].filter(user=self.request.user)
        return context



class Habits(LoginRequiredMixin, ListView):
    model = Habit
    template_name = 'habit_list.html'
    context_object_name = 'habits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = GroupOfHabits.objects.all()
        context['habits'] = context['habits'].filter(user=self.request.user)
        return context


class HabitCreate(LoginRequiredMixin, CreateView):
    model = Habit
    fields = '__all__'
    success_url = reverse_lazy('habit')


class HabitDelete(LoginRequiredMixin, DeleteView):
    model = Habit
    context_object_name = 'habit'
    success_url = reverse_lazy('habit')


class WeekOfHabitCreate(LoginRequiredMixin, CreateView):
    model = WeekOfHabit
    fields = ['habit']
    success_url = reverse_lazy('table')
    template_name = 'table/week_habit_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WeekOfHabitCreate, self).form_valid(form)


class WeekOfHabitUpdate(LoginRequiredMixin, UpdateView):
    model = WeekOfHabit
    fields = '__all__'
    success_url = reverse_lazy('table')
    template_name = 'table/week_habit_form.html'


class WeekHabitDelete(LoginRequiredMixin, DeleteView):
    model = WeekOfHabit
    context_object_name = 'habit'
    success_url = reverse_lazy('table')



class GroupOfHabitCreate(LoginRequiredMixin, CreateView):
    model = GroupOfHabits
    fields = ['name']
    success_url = reverse_lazy('habit')
    template_name = 'group/group_form.html'


class GroupOfHabitDelete(LoginRequiredMixin, DeleteView):
    model = GroupOfHabits
    context_object_name = 'group'
    success_url = reverse_lazy('habit')
    template_name = 'group/group_confirm_delete.html'





