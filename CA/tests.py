from django.test import TestCase

class CaFilterViewTests(TestCase):
     def test_filter_uses_query_parameters(self):
         response = self.client.get('/filter/?genre=action&year=2025')
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, 'action')
         self.assertContains(response, '2025')

class HomeTest(TestCase):
     def test_home(self):
          self.assertEqual(2+2,4)
