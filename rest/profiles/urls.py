from django.urls import path
from profiles.views import UserProfileView


urlpatterns = [
    path('authentication/', UserProfileView.as_view()),
    ]