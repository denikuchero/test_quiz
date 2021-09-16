from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from rest_api.models import Quiz
from rest_api.serializers import QuizSerializer


class QuizApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.quiz_1 = Quiz.objects.create(name='Квиз 1', description = 'описание для квиза 1')
        self.quiz_2 = Quiz.objects.create(name='Квиз 2', description = 'описание для квиза 2')

    def test_get(self):
        url = reverse('quiz')
        response = self.client.get(url)
        serializer_data = QuizSerializer([self.quiz_1,self.quiz_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(QuizSerializer([self.quiz_1,self.quiz_2], many=True).data, self.client.get(reverse('quiz')).data)




