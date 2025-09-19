from django.db import models
from langleveltopics.models import Language, Level, Topic


class Lesson(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    intro = models.JSONField(default=dict)  # {"title": "...", "paragraph": "..."}
    body = models.JSONField(default=list)   # [{"title": "X", "text": "Y"}, ...]

    def __str__(self):
        return f"Lesson: {self.topic.key} ({self.language.iso_code}, {self.level.code})"


class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="exercises")
    topics = models.ManyToManyField(Topic)
    levels = models.ManyToManyField(Level)
    prompt = models.TextField()
    solutions = models.JSONField(default=list)  # [{"answer": "cat", "correct": True}, ...]

    def __str__(self):
        return f"Exercise for lesson {self.lesson.id}"
