from django.urls import reverse, resolve
from quizapp.views import question, result_list, quiz
from django.test import TestCase, SimpleTestCase


class TestUrls(SimpleTestCase):
    def test_quiz_resolves(self):
        url = reverse('quiz')
        self.assertEquals(resolve(url).func, quiz)

    def test_result_list_resolves(self):
        url = reverse('results')
        self.assertEquals(resolve(url).func, result_list)

    def test_question_resolve(self):
        url = reverse('question', kwargs={'pk':1})
        self.assertEquals(resolve(url).func, question)
