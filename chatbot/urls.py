from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/', views.chatbot_recommendations, name='chatbot_recommendations'),
]
