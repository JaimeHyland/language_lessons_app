from rest_framework import serializers
from .models import Language, LangName, Level, Topic


class LanguageSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = Language
        fields = ["id", "iso_code", "display_name"]

    def get_display_name(self, obj):
        request = self.context.get("request")
        lang_iso = request.query_params.get("lang_iso") if request else None

        if lang_iso:
            # Look up LangName with text_iso == lang_iso
            name = obj.names.filter(text_iso__iso_code=lang_iso).first()
            if name:
                return name.name_text

        # fallback: iso_code
        return obj.iso_code


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ["id", "code", "order"]


class TopicSerializer(serializers.ModelSerializer):
    theme_name = serializers.CharField(source="theme.name", read_only=True)
    language_iso = serializers.CharField(source="theme.language.iso_code", read_only=True)
    level_code = serializers.CharField(source="level.code", read_only=True)

    class Meta:
        model = Topic
        fields = [
            "id",
            "key",
            "native_name",
            "foreign_names",
            "order",
            "theme_name",
            "language_iso",
            "level",
            "level_code",
        ]
