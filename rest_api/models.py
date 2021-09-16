from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# from rest_framework.authtoken.admin import User





class Quiz(models.Model):
    """
    модель квиза
    """
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Questons(models.Model):
    """
    Вопросы квиза.
    type_question (0-один вариант ответа, 1 - несколько варинатов, 2 - текстовый ответ)
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    type_questions = models.PositiveSmallIntegerField(default=0)



class AnsewerQuestins(models.Model):
    """
    варианты ответа на вопросы в квизе
    """
    question = models.ForeignKey(Questons, on_delete=models.CASCADE)
    answer_option = models.CharField(max_length=255, null=True)


# ----------------------------------------------------------------------------------------------------------------------

class AnswerUser(models.Model):
    """
    ответы пользователя на квиз
    """
    id_user = models.CharField(max_length=12)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True)


class ListAnswerUser(models.Model):
    """
    Список ответов пользователя на вопросы
    """
    answer_user = models.ForeignKey(AnswerUser, on_delete=models.CASCADE)
    answer_questions = models.ForeignKey(Questons, on_delete=models.CASCADE)
    answer_options = models.ForeignKey(AnsewerQuestins, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)



