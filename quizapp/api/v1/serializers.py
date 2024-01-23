from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from quizapp.models import QuizType, Result
from django.contrib.auth import get_user_model
from .exepstions import OldPasseordExepstions

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta(object):
        model = User
        fields = ('username', 'password', 'email')


class QuizTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizType
        fields = ['id', 'name']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise OldPasseordExepstions()
        return value
