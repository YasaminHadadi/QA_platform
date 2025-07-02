from rest_framework import serializers
from .models import Question, Answer
from django.contrib.auth import get_user_model

User = get_user_model()


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Answer
        fields = '__all__'



class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    answers_list = AnswerSerializer(many=True, read_only=True, source='answers')
    class Meta:
        model = Question
        fields = ['id', 'user', 'title', 'body', 'created_at', 'answers_list']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
