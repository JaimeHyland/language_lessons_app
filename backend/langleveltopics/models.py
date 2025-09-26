from django.db import models


class Language(models.Model):
    iso_code = models.CharField(max_length=10, unique=True)  # e.g. "de_DE"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.iso_code


class LangName(models.Model):
    name_text = models.CharField(max_length=200)
    lang_iso = models.ForeignKey("langleveltopics.Language", on_delete=models.CASCADE, related_name="names")
    text_iso = models.ForeignKey("langleveltopics.Language", on_delete=models.CASCADE, related_name="translations")

    class Meta:
        unique_together = ("lang_iso", "text_iso")
        verbose_name = "Language name"

    def __str__(self):
        return f"{self.name_text} ({self.text_iso.iso_code}) → {self.lang_iso.iso_code}"


class Level(models.Model):
    code = models.CharField(max_length=2, unique=True)  # A1, A2, ...
    order = models.PositiveSmallIntegerField(help_text="Ordering for levels (1..6)")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.code


class Theme(models.Model):
    # The language this theme is about (theme belongs to a single language)
    language = models.ForeignKey("langleveltopics.Language", on_delete=models.CASCADE, related_name="themes")
    key = models.CharField(max_length=100)  # stable internal id, e.g. "adjectives"
    native_name = models.CharField(max_length=200)  # name in the theme's language
    foreign_names = models.JSONField(default=dict, blank=True)
    # example: {"en_GB": "Adjectives and Adverbs", "es_ES": "Adjetivos"}

    class Meta:
        unique_together = ("language", "key")

    def __str__(self):
        return f"{self.native_name} ({self.language.iso_code})"


class Topic(models.Model):
    theme = models.ForeignKey("langleveltopics.Theme", on_delete=models.CASCADE, related_name="topics")
    # The level for the topic (A1..C2)
    level = models.ForeignKey("langleveltopics.Level", on_delete=models.CASCADE, related_name="topics")

    key = models.CharField(max_length=100)
    native_name = models.CharField(max_length=200)
    foreign_names = models.JSONField(default=dict, blank=True)
    order = models.PositiveSmallIntegerField(default=1, help_text="Ordering within the level/theme")

    class Meta:
        unique_together = ("theme", "level", "key")
        ordering = ["level__order", "order"]

    def __str__(self):
        return f"{self.native_name} ({self.theme.language.iso_code}, {self.level.code})"

    def available_languages(self):
        """Return list of language iso_codes in which the topic has sections."""
        return list(self.sections.values_list("language__iso_code", flat=True).distinct())


class Section(models.Model):
    # Section belongs to one Topic and is written in a particular explanation language
    topic = models.ForeignKey("langleveltopics.Topic", on_delete=models.CASCADE, related_name="sections")
    language = models.ForeignKey("langleveltopics.Language", on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

    class Meta:
        ordering = ["order"]
        unique_together = ("topic", "language", "order")

    def __str__(self):
        return f"{self.topic.key} [{self.language.iso_code}] - {self.heading or 'Section'}"
