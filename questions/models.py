from django.db import models


class Question(models.Model):
    class QuestionType(models.TextChoices):
        MULTIPLE = "multiple", "ONE CORRECT ANSWER AND SEVERAL INCORRECT ANSWERS"
        BOOLEAN = "boolean", "TRUE OR FALSE"

    class LevelDifficulty(models.TextChoices):
        EASY = "easy"
        MEDIUM = "medium"
        HARD = "hard"

    type = models.CharField(max_length=10, choices=QuestionType.choices)
    difficulty = models.CharField(max_length=10, choices=LevelDifficulty.choices)
    category = models.CharField(max_length=100)
    question = models.TextField(max_length=1000)
    correct_answer = models.TextField(max_length=255)
    incorrect_answers = models.JSONField()

    def __str__(self):
        return self.question
