from django.shortcuts import render
from .models import WeekOfHabit, GroupOfHabits, Habit, Notes
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


def home(request):
    """View of home page."""
    return render(request, 'home.html')


def contact(request):
    """View of contact page."""
    return render(request, 'contact.html')


class TableOfWeek(LoginRequiredMixin, ListView):
    """View for table of habits."""
    model = Habit
    template_name = 'table_of_week.html'
    context_object_name = 'base_habits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habits'] = WeekOfHabit.objects.all()
        context['habits'] = context['habits'].filter(user=self.request.user)
        return context


class Habits(LoginRequiredMixin, ListView):
    """View for habits page with list of all habits and habit's groups."""
    model = Habit
    template_name = 'habit_list.html'
    context_object_name = 'habits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = GroupOfHabits.objects.all()
        context['habits'] = context['habits'].filter(user=self.request.user)
        return context


class HabitCreate(LoginRequiredMixin, CreateView):
    """Create new habit."""
    model = Habit
    fields = ['name', 'group']
    success_url = reverse_lazy('habit')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(HabitCreate, self).form_valid(form)


class HabitDelete(LoginRequiredMixin, DeleteView):
    """Delete habit."""
    model = Habit
    context_object_name = 'habit'
    success_url = reverse_lazy('habit')


class WeekOfHabitCreate(LoginRequiredMixin, CreateView):
    """Create new habit in table of week."""
    model = WeekOfHabit
    fields = ['habit']
    success_url = reverse_lazy('table')
    template_name = 'table/week_habit_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WeekOfHabitCreate, self).form_valid(form)


class WeekOfHabitUpdate(LoginRequiredMixin, UpdateView):
    """Update a habit in table of week."""
    model = WeekOfHabit
    fields = ['monday', 'monday_hours', 'tuesday', 'tuesday_hours', 'wednesday', 'wednesday_hours', 'thursday',
              'thursday_hours', 'friday', 'friday_hours', 'saturday', 'saturday_hours', 'sunday', 'sunday_hours']
    success_url = reverse_lazy('table')
    template_name = 'table/week_habit_form.html'


class WeekHabitDelete(LoginRequiredMixin, DeleteView):
    """Delete a habit from table of week."""
    model = WeekOfHabit
    context_object_name = 'habit'
    success_url = reverse_lazy('table')


class GroupOfHabitCreate(LoginRequiredMixin, CreateView):
    """Create new group of habits."""
    model = GroupOfHabits
    fields = ['name']
    success_url = reverse_lazy('habit')
    template_name = 'group/group_form.html'


class GroupOfHabitDelete(LoginRequiredMixin, DeleteView):
    """Delete a group of habits."""
    model = GroupOfHabits
    context_object_name = 'group'
    success_url = reverse_lazy('habit')
    template_name = 'group/group_confirm_delete.html'


class Notess(LoginRequiredMixin, ListView):
    """View for notes page."""
    model = Notes
    template_name = 'notes.html'
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.all()
        context['notes'] = context['notes'].filter(user=self.request.user)
        return context


class NotesCreate(LoginRequiredMixin, CreateView):
    """Create new note."""
    model = Notes
    fields = ['habit', 'title', 'slug', 'body']
    template_name = 'notes/notes_form.html'
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NotesCreate, self).form_valid(form)


class NotesDelete(LoginRequiredMixin, DeleteView):
    """Delete a note."""
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_confirm_delete.html'
    success_url = reverse_lazy('notes')

