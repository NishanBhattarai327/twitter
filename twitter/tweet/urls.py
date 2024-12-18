from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tweets, name="all_tweets"),
    path('tweet/', views.tweet, name='tweet'),
    path('<int:tweet_id>/tweet_edit/', views.tweet_edit, name="tweet_edit"),
    path('<int:tweet_id>/tweet_delete/', views.tweet_delete, name="tweet_delete"),
    path('register/', views.register, name="register"),
]
