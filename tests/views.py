from django.shortcuts import get_object_or_404, render

from .models import Choice, Test


def index(request):
    """Функция главной страницы, отдаёт список существующих тестов"""
    question_list = Test.objects.all()
    return render(request, "index.html", {"question_list": question_list})


def test_view(request, test_id):
    """Функция отображения теста и его вопросов для прохождения"""
    test = get_object_or_404(Test, id=test_id)
    return render(request, "test.html", {"test": test})


def new_test_results(request, test_id):
    """Функция для проверки теста, сохранения и вывода результата"""
    choice = Choice.objects.all()
    test = get_object_or_404(Test, id=test_id)

    right_answers = 0
    for question_id, answer in request.POST.items():
        for name in choice:
            if name.title == answer:
                if name.points > 0:
                    right_answers += 1

    wrong_answers = test.max_points - right_answers
    percent_right_answers = (right_answers / test.max_points) * 100
    pricent_wrong_answers = (wrong_answers / test.max_points) * 100

    if percent_right_answers >= 50:
        result = "Тест пройден"
    else:
        result = "Тест не пройден"

    context = {
        "test": test,
        "right_answers": right_answers,
        "wrong_answers": wrong_answers,
        "percent_right_answers": percent_right_answers,
        "pricent_wrong_answers": pricent_wrong_answers,
        "result": result,
    }
    return render(request, "results.html", context)
