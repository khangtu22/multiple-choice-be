from django.urls import path
from questions import views

urlpatterns = [
    path("", views.ListQuestionAPIView.as_view(), name="question_list"),
    path("create/", views.CreateQuestionAPIView.as_view(), name="question_create"),
    path("update/<int:pk>/", views.UpdateQuestionAPIView.as_view(), name="update_question"),
    path("delete/<int:pk>/", views.DeleteQuestionAPIView.as_view(), name="delete_question"),
    path("random/", views.RandomQuestionAPIView.as_view(), name="random_question"),
    path("<str:question_id>/", views.GetQuestionAPIView.as_view(), name="get_question_by_id"),
    path('<str:question_id>/choices/', views.GetChoiceByQuestionIDAPIView.as_view(),
         name='choices-by-question-id'),
]
