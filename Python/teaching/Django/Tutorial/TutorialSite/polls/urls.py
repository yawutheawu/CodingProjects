from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("specifics/<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

urlpatterns += staticfiles_urlpatterns()