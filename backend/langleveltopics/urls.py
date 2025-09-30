from django.urls import path
from . import views

urlpatterns = [
    path('api/languages/', views.LanguageList.as_view(), name='language-list'),
    path('api/levels/', views.LevelList.as_view(), name='level-list'),
    path('api/topics/', views.TopicList.as_view(), name='topic-list'),
]
