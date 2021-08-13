from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    test = models.ForeignKey("Test", on_delete=models.CASCADE)
    points = models.IntegerField()

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.test


class Question(models.Model):
    title = models.CharField(max_length=500)
    choice = choice = models.ManyToManyField(
        "Choice",
        through="ChoiceItem",
        through_fields=("question", "choice"),
        related_name="question",
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title


class Choice(models.Model):
    title = models.CharField(max_length=4096)
    points = models.IntegerField()

    class Meta:
        verbose_name = "Выбор"
        verbose_name_plural = "Выборы"

    def __str__(self):
        return self.title


class ChoiceItem(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="question_item",
    )
    choice = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name="choice_item"
    )

    def __str__(self):
        return self.choice.title


class Test(models.Model):
    title = models.CharField(max_length=500)
    question = models.ManyToManyField(
        Question,
        related_name="question_test",
    )
    max_points = models.IntegerField()

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.title
