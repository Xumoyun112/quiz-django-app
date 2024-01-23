from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action

from .serializers import QuizTypeSerializer, ResultSerializer, ChangePasswordSerializer, UserSerializer
from quizapp.models import QuizType, Question, Result, User
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from rest_framework import filters


@api_view(['GET'])
def hello_world(request):
    data = {'message': 'Hello World!'}
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def quiz_types(request):
    if request.method == 'GET':
        quiz_types = QuizType.objects.all()
        serializer = QuizTypeSerializer(quiz_types, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = QuizTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def quiz_type(request):
    if request.method == 'GET':
        quiz_types = QuizType.objects.all()
        serializer = QuizTypeSerializer(quiz_types)
        return Response(data=serializer.data, status=status)
    if request.method == 'PUT':
        serializer = QuizTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizType.objects.all()
    # permission_classes = []
    authentication_classes = []
    serializer_class = QuizTypeSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     search = self.request.query_params.get('search')
    #     if search:
    #         qs = qs.filter(name=search)
    #     return qs

    @action(detail=False, url_path='result-list', authentication_classes=[TokenAuthentication])
    def results(self, request):
        if request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        results = Result.objects.filter(user=request.user.id)
        serializer = ResultSerializer(results, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST', 'PUT'])
    def change_password(self, request):
        user = self.request.user
        serializer = ChangePasswordSerializer(user, request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            return Response({'mess': 'password changed'}, status=status.HTTP_200_OK)
        return Response({'mess': 'error'}, status=status.HTTP_400_BAD_REQUEST)
