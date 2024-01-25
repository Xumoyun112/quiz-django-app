from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase
from quizapp.api.v1.views import QuestionViewSet, quiz_types

class TestQuestionViewSet(TestCase):
    def setUp(self):
        self.url = reverse('')