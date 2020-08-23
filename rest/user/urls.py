from django.urls import path
from user.views import UserRegistrationView, UserLoginView
from profiles.views import UserProfileView

urlpatterns = [
    path('signup/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    #path('profile/', UserProfileView.as_view()),
    ]
