from django.urls import path

from apps.users.views import UserListView, UserDetailView, Login, LoginOtp, LoginConfirm

urlpatterns = [
    path("", UserDetailView.as_view(), name="user-detail"),
    path("list/", UserListView.as_view(), name="user-list"),
    path("login/", Login.as_view(), name="login"),
    path("login-otp/", LoginOtp.as_view(), name="login-otp"),
    path("login-confirm/", LoginConfirm.as_view(), name="login-confirm"),
]
