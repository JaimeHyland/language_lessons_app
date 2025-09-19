from django.db import models


class Language(models.Model)
    ISO_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.ISO_code


class LangName(models.Model):
    NameText = models.CharField(max_length=100)
    Lang_ISO = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="names")
    Text_ISO = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="translations")

    class Meta:
        unique_together = ("Lang_ISO", "Text_ISO")  # prevent duplicates

    def __str__(self):
        return f"{self.NameText} ({self.Text_ISO.ISO_code}) → {self.Lang_ISO.ISO_code}"


class Level(models.Model):
    code = models.CharField(max_length=2, unique=True)  # A1, A2, B1...
    order = models.PositiveSmallIntegerField()  # 1–6, for ordering

    def __str__(self):
        return self.code


class Topic(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)  # stable identifier
    names = models.JSONField(default=dict)  # e.g., {"en_GB": "Travel", "de_DE": "Reisen"}

    def __str__(self):
        return f"{self.key} ({self.language.iso_code})"