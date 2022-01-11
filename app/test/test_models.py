from django.test import TestCase
from habits.models import GroupOfHabits


class ModelsTestCase(TestCase):
    def test_group_creation(self):
        group = GroupOfHabits.objects.create(name="My first habit")
        group.save()
        self.assertEqual(group.name, "My first habit")

