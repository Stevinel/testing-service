from django.contrib import admin

from .models import Answer, Choice, ChoiceItem, Question, Test


class QuestionInline(admin.TabularInline):
    model = ChoiceItem
    fields = ["question", "choice"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("user", "test", "created", "points")
    search_fields = ("question", "points")
    list_filter = ("created",)
    empty_value_display = "-пусто-"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ("title",)
    inlines = [QuestionInline]
    empty_value_display = "-пусто-"


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("title", "points")
    search_fields = ("title",)
    list_filter = ("title",)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    model = Test
    fields = ["title", "question", "max_points"]
    search_fields = ("question", "max_points")
