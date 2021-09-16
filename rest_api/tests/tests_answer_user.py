from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.test import Client

from rest_api.models import Quiz, Questons, AnswerUser, ListAnswerUser, AnsewerQuestins
from rest_api.serializers import QuizSerializer, AnswerUserSerializer, ListAnswerUserSerializer


class AnswerUserApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.quiz_1 = Quiz.objects.create(name='Квиз 1', description = 'описание для квиза 1')
        self.question = Questons.objects.create(quiz= self.quiz_1,
                                                question= "Вопрос номер 1",
                                                type_questions = 0)

        self.question_for_answer = Questons.objects.get(id=1)
        self.ansewer_for_questins_1 = AnsewerQuestins.objects.create(question= self.question_for_answer,
                                                answer_option= "Вариант ответа номер 1",
                                               )
        self.ansewer_for_questins_2 = AnsewerQuestins.objects.create(question= self.question_for_answer,
                                                answer_option= "Вариант ответа номер 2",
                                               )


        self.get_quiz = Quiz.objects.get(id=1)
        print('self.get_quiz', self.get_quiz)

        self.url = reverse('get_id_user')
        self.response = self.client.get(self.url)
        self.create_answer_user = AnswerUser.objects.create(
            id_user = self.response.data['id_user'],
            quiz = self.quiz_1
        )


        self.answer_user = AnswerUser.objects.get(id=1)
        self.answer_questions = Questons.objects.get(id=1)
        self.answer_options = AnsewerQuestins.objects.get(id=1)

        self.create_answer_question_user = ListAnswerUser.objects.create(
            answer_user = self.answer_user,
            answer_questions = self.answer_questions,
            answer_options = self.answer_options,
            answer_text = '',
        )


    def test_get(self):

        self.assertEqual(QuizSerializer([self.quiz_1, ], many=True).data, self.client.get(reverse('quiz')).data)
        self.assertEqual(AnswerUserSerializer([self.create_answer_user, ], many=True).data, self.client.get(reverse(
            'get_quiz_user'), data={'id_user': self.response.data['id_user'] }).data)
        self.assertEqual(ListAnswerUserSerializer([self.create_answer_question_user, ], many=True).data, self.client.get(reverse(
            'get_quiz_answers_user'), data={'id_answer_user': 1 }).data)
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)


