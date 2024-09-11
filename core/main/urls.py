from django.urls import path

from apps.users.views import UserDetailView, Login, LoginOtp, LoginConfirm

urlpatterns = [
    path("", UserDetailView.as_view()),
    path("login/", Login.as_view()),
    path("login-otp/", LoginOtp.as_view()),
    path("login-confirm/", LoginConfirm.as_view()),
]
