from django.urls import path

from .views import hello_world, quiz_types, QuestionViewSet, UserModelViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'questions', QuestionViewSet, basename='questionview')
router.register(r'users', UserModelViewSet, basename='usermodelview')

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('types/', quiz_types, name='quiz_types')
]

urlpatterns += router.urls
