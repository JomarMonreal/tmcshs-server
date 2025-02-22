from django.urls import path
from .views import LoginView, LogoutView, UserRegistrationView, verify_token

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/', verify_token, name='verify-token'),
]
