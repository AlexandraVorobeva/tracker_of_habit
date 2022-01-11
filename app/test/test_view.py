from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_view_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_view_table(self):
        response = self.client.get('/table/')
        self.assertEqual(response.status_code, 302)

    def test_view_habit(self):
        response = self.client.get('/habit/')
        self.assertEqual(response.status_code, 302)

    def test_view_notes(self):
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, 302)

