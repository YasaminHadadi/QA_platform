from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.QuestionListCreateView.as_view(), name='question-list'),
    path('question/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('answers/', views.AnswerListCreateView.as_view(), name='answer-list'),
    path('answers/<int:pk>/', views.AnswerListCreateView.as_view(), name='answer-detail'),
]