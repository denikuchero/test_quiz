
from django.urls import path, re_path
from .views import *
from rest_framework.routers import SimpleRouter
from django.conf.urls import  include, url
from rest_framework_jwt import views as jwt_views

router = SimpleRouter()

# router.register(r'quiz', QuizViewSet)



urlpatterns = [
    path('quiz/', ListQuizViewSet.as_view(), name='quiz'),
    path('quiz_is_active/', ListQuizisActiveViewSet.as_view(), name='quiz_is_active'),
    path("create_quiz/", CreateQuizViewSet.as_view(), name="create_quiz"),
    path("update_quiz/<int:id>/", UpdateQuizViewSet.as_view(), name="update_quiz"),
    path("update_quiz_is_active_false/<int:id>/", UpdateQuizisActiveFalseViewSet.as_view(), name="update_quiz_is_active_false"),
    path("update_quiz_is_active_true/<int:id>/", UpdateQuizisActiveTrueViewSet.as_view(),
         name="update_quiz_is_active_true"),
    path("delete_quiz/<int:id>/", DeleteQuizViewSet.as_view(), name="delete_quiz"),

    path('quiz/<int:id_quize>/question/', ListQuestionViewSet.as_view(), name='question'),
    path('quiz/create_question/', CreateQuestionViewSet.as_view(), name='create_question'),

    path('quiz/answer_question/<int:id_question>', ListAnsewerQuestinsViewSet.as_view(), name='answer_question'),
    path('quiz/create_answer_question/', CreateAnsewerQuestinsViewSet.as_view(), name='create_answer_question'),

    path('user/get_id_user/', GetIdUserViewSet.as_view(), name='get_id_user'),
    path('user/answer_user/', CreateAnswerUserViewSet.as_view(), name='answer_user'),
    path('user/answer_question_user/', CreateListAnswerUserViewSet.as_view(), name='answer_question_user'),

    # path('user/get_quiz_user/<str:id_user>', GetQuizUser.as_view(), name='get_quiz_user'),
    re_path(r'user/get_quiz_user/$', GetQuizUser.as_view(), name='get_quiz_user'),
    re_path(r'user/get_quiz_answers_user/$', GetListAnswersUserUser.as_view(), name='get_quiz_answers_user'),

    re_path(r'^account/', include('djoser.urls')),
    re_path(r'^auth/login/', jwt_views.obtain_jwt_token, name='auth'),


]

urlpatterns += router.urls