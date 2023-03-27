from django.urls import path
from choices import views

urlpatterns = [
    path("", views.ListChoiceAPIView.as_view(), name="choice_list"),
    path("create/", views.CreateChoiceAPIView.as_view(), name="choice_create"),
    path("update/<int:pk>/", views.UpdateChoiceAPIView.as_view(), name="update_choice"),
    path("delete/<int:pk>/", views.DeleteChoiceAPIView.as_view(), name="delete_choice"),
]
