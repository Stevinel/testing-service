from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/", include("django.contrib.auth.urls")),
    path(
        "results/<int:test_id>",
        views.new_test_results,
        name="new_test_results",
    ),
    path("test/<int:test_id>", views.test_view, name="test"),
]
