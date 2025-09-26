from django.contrib import admin
from .models import Language, Level, LangName, Theme, Topic, Section


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'iso_code', 'created_at')
    ordering = ('id',)
    search_fields = ("iso_code",)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "order")
    search_fields = ("code",)
    ordering = ("order",)


@admin.register(LangName)
class LangNameAdmin(admin.ModelAdmin):
    list_display = ('name_text', 'lang_iso', 'text_iso')
    list_filter = ('lang_iso', 'text_iso')
    search_fields = ('name_text',)

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'native_name', 'language_id')
    search_fields = ('key', 'native_name')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'native_name', 'theme', 'order',)
    list_editable = ("order",)
    search_fields = ('key', 'native_name')

    fieldsets = (
        ("Core info", {
            "fields": ("key", "native_name", "theme", "level"),
        }),
        ("Extra translations", {
            "fields": ("foreign_names",),
            "classes": ("collapse",),  # makes it collapsible
        }),
    )

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'heading', 'text')
    list_filter = ('topic',)
    search_fields = ('heading', 'text')
