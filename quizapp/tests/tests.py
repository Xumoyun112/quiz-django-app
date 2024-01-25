# from django.test import TestCase, SimpleTestCase
# from django.urls import reverse, resolve
#
#
# class TestHelloWorld(TestCase):
#     def setUp(self) -> None:
#         self.url = reverse('hello_world')
#
#     def test_gets(self):
#         response = self.client.get(self.url)
#         assert response.status_code == 200
#         assert response.json()['message'] == 'hello world!'
#
#
# class TestQuiztype(TestCase):
#     def setUp(self):
#         self.url = reverse('quiz_types')
#
#     def test_get_is_valid(self):
#         data = {
#             'name': 'Test'
#         }
#         response = self.client.get(self.url)
#         assert response.status_code == 200