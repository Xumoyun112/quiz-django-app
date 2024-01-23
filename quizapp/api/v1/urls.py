from django.urls import path

from .views import hello_world, quiz_types, QuestionViewSet, UserModelViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'questions', QuestionViewSet)
router.register(r'users', UserModelViewSet)

urlpatterns = [
    path('', hello_world),
    path('types/', quiz_types)
]

urlpatterns += router.urls
