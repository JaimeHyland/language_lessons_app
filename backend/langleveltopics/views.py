from rest_framework import generics
from .models import Language, Level, Topic
from .serializers import LanguageSerializer, LevelSerializer, TopicSerializer


class LanguageList(generics.ListAPIView):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        language_iso = self.request.query_params.get('lang_iso', None)
        queryset = Language.objects.all()
        if language_iso:
            queryset = queryset.filter(names__text_iso__iso_code=language_iso)
        return queryset


class LevelList(generics.ListAPIView):
    queryset = Level.objects.all().order_by("order")
    serializer_class = LevelSerializer


class TopicList(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        language_iso = self.request.query_params.get("language_iso")
        level_id = self.request.query_params.get("level_id")

        queryset = Topic.objects.all()

        if language_iso:
            queryset = queryset.filter(theme__language__iso_code=language_iso)
        if level_id:
            queryset = queryset.filter(level_id=level_id)

        return queryset
