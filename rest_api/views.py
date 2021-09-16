import hashlib
import random
import time

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from django.contrib.auth import authenticate


from rest_api.models import Quiz, Questons, AnsewerQuestins, AnswerUser, ListAnswerUser
from rest_api.serializers import QuizSerializer, UserSerializer, QuestonsSerializer, AnsewerQuestinsSerializer, \
    AnswerUserSerializer, GetIdUserSerializer, ListAnswerUserSerializer


class ListQuizViewSet(ListAPIView):
    """Список квизов"""
    permission_classes = [AllowAny]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class CreateQuizViewSet(CreateAPIView):
    """Создаем новый квиз"""
    permission_classes = [AllowAny]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class UpdateQuizViewSet(UpdateAPIView):
    """Обновляем данные"""
    permission_classes = [AllowAny]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'id'

class DeleteQuizViewSet(DestroyAPIView):
    """Удаляем квиз"""
    permission_classes = [AllowAny]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'id'
#     -----------------------------------------------------------------------------------------------


class ListQuestionViewSet(ListAPIView):
    """Список вопросво в квизе"""
    permission_classes = [AllowAny]
    # lookup_field = 'id'
    serializer_class = QuestonsSerializer

    def get_queryset(self):
        print(self.kwargs)
        id_quize = self.kwargs['id_quize']
        queryset = Questons.objects.filter(quiz=id_quize)
        return queryset

class CreateQuestionViewSet(CreateAPIView):
    """Список вопросво в квизе"""
    permission_classes = [AllowAny]
    serializer_class = QuestonsSerializer

class UpdateQuestionViewSet(UpdateAPIView):
    """Обновляем данные"""
    permission_classes = [AllowAny]
    queryset = Questons.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'quiz'

class DeleteQuestionViewSet(DestroyAPIView):
    """Удаляем квиз"""
    permission_classes = [AllowAny]
    queryset = Questons.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'quiz'

#     -----------------------------------------------------------------------------------------------

class ListAnsewerQuestinsViewSet(ListAPIView):
    """Список ответов для вопроса"""
    permission_classes = [AllowAny]
    # lookup_field = 'id'
    serializer_class = AnsewerQuestinsSerializer

    def get_queryset(self):
        print(self.kwargs)
        id_question = self.kwargs['id_question']

        queryset = AnsewerQuestins.objects.filter(question=id_question)
        return queryset


class CreateAnsewerQuestinsViewSet(CreateAPIView):
    """Создаем список ответов на вопрос"""
    permission_classes = [AllowAny]
    serializer_class = AnsewerQuestinsSerializer


class UpdateAnsewerQuestinsViewSet(UpdateAPIView):
    """Обновляем данные"""
    permission_classes = [AllowAny]
    queryset = AnsewerQuestins.objects.all()
    serializer_class = AnsewerQuestinsSerializer
    lookup_field = 'question'

class DeleteAnsewerQuestinsViewSet(DestroyAPIView):
    """Удаляем вопрос"""
    permission_classes = [AllowAny]
    queryset = AnsewerQuestins.objects.all()
    serializer_class = AnsewerQuestinsSerializer
    lookup_field = 'question'

#     -----------------------------------------------------------------------------------------------

class ListQuizisActiveViewSet(ListAPIView):
    """Список активных квизов (по которым можно дальше вытащить все вопросы, и ответы к ним) """
    permission_classes = [AllowAny]
    serializer_class = QuizSerializer

    def get_queryset(self):
        queryset = Quiz.objects.filter(is_active=True)
        return queryset

class UpdateQuizisActiveFalseViewSet(UpdateAPIView):
    """изменение статуса активности квиза на неактивный"""

    permission_classes = [AllowAny]
    serializer_class = QuizSerializer
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = Quiz.objects.filter(id=id).update(is_active=False)
        return queryset


class UpdateQuizisActiveTrueViewSet(UpdateAPIView):
    """изменение статуса активности квиза на активный"""

    permission_classes = [AllowAny]
    serializer_class = QuizSerializer
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = Quiz.objects.filter(id=id).update(is_active=True)
        return queryset


"""
- Прохождение теста
- получение результатов пройденных вопросов
AnswerUser
"""


class GetIdUserViewSet(APIView):
    """
    Возвращает уникальный id пользователя для прохождения теста.
    случайный id если пользователь не авторизован
    id пользователя если авторизован
    """
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    # serializer_class = GetIdUserSerializer

    def get_queryset(self):
        return None

    def get(self, request):
        if request.user.is_anonymous:
            id_user_hash = hashlib.md5((random.randrange(0, 1000) + int(time.time())).to_bytes(10,'big'))
            id_user = id_user_hash.hexdigest()[:10]
        else:
            id_user = self.request.user.id

        serializer = GetIdUserSerializer( many=True)
        serializer.id_user = id_user

        return Response({'id_user': serializer.id_user} )



class CreateAnswerUserViewSet(CreateAPIView):
    """Создает запись в базе данных о новом квизе пользователя"""
    permission_classes = [AllowAny]
    serializer_class = AnswerUserSerializer


class CreateListAnswerUserViewSet(CreateAPIView):
    """Записывает ответы пользователя в базу"""
    permission_classes = [AllowAny]
    serializer_class = ListAnswerUserSerializer


class GetQuizUser(ListAPIView):
    """
    запрос для получения списка квизов у пользователя
    """
    permission_classes = [AllowAny]
    serializer_class = AnswerUserSerializer

    # id_user = acf4d79f19

    def get_queryset(self):

        print(self.request.query_params['id_user'])
        id_user = self.request.query_params['id_user']
        queryset = AnswerUser.objects.filter(id_user=id_user)

        return queryset


class GetListAnswersUserUser(ListAPIView):
    """
    запрос для получения списка ответов пользователя по нужному квизу
    """
    permission_classes = [AllowAny]
    serializer_class = ListAnswerUserSerializer

    # id_user = acf4d79f19
    def get_queryset(self):
        id_answer_user = self.request.query_params['id_answer_user']
        queryset = ListAnswerUser.objects.filter(answer_user=id_answer_user)


        return queryset


