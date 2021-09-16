from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


description = """
API для проведения опросов.

Функционал:
- создание опроса (добавление, удаление, изменение)
- создание вопросов (добавление, удаление, изменение)
- отображение опросов пользователя
- отображение списка ответов пользователя
- опросы может проходить анонимный пользователь, и зарегистрированный

      """



schema_view = get_schema_view(
   openapi.Info(
      title="API quiz",
      default_version='v1',
      description=description,
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   re_path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='api_redoc'),
]