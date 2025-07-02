from rest_framework import serializers
from .models import Question, Answer



class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Answer
        fields = '__all__'



class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    answers_list = AnswerSerializer(many=True, read_only=True, source='answers')
    class Meta:
        model = Question
        fields = ['id', 'user', 'title', 'body', 'created_at', 'answers_list']

