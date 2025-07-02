from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.QuestionListCreateView.as_view(), name='question-list'),
    path('question/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('answers/', views.AnswerListCreateView.as_view(), name='answer-list'),
    path('answer/<int:pk>/', views.AnswerDetailView.as_view(), name='answer-detail'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
]