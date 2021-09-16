from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from rest_api.models import Quiz, Questons, AnsewerQuestins, AnswerUser, ListAnswerUser


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestonsSerializer(ModelSerializer):
    class Meta:
        model = Questons
        fields = '__all__'


class AnsewerQuestinsSerializer(ModelSerializer):
    class Meta:
        model = AnsewerQuestins
        fields = '__all__'


class AnswerUserSerializer(ModelSerializer):
    class Meta:
        model = AnswerUser
        fields = '__all__'

class GetIdUserSerializer(serializers.Serializer):
    id_user = serializers.CharField(max_length=12)

    class Meta:
        fields = ['id_user']


class ListAnswerUserSerializer(ModelSerializer):
    class Meta:
        model = ListAnswerUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (['username' ])