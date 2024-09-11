import uuid
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import (
    TokenAuthentication as RestTokenAuthentication,
)
from rest_framework.views import APIView

from .models import Company, User
from .serializers import UserDetailSerializer
from .authentication import TokenAuthentication
from .utils import generate_token, generate_code
from .serializers import LoginConfirmSerializer

from django.core.cache import cache


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [RestTokenAuthentication]

    def get_object(self):
        return self.request.user


class Login(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, _ = User.objects.get_or_create(
            telephone=serializer.validated_data["telephone"], username=uuid.uuid4()
        )

        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user, token=generate_token())
        return Response({"token": token.token, "user_id": user.pk})


class LoginOtp(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = generate_code()
        if cache.keys(f'otp_{serializer.validated_data["telephone"]}'):
            return Response({"data": "sms_already_sent"})

        cache.set(f'otp_{serializer.validated_data["telephone"]}', code, 60 * 2)

        return Response({"data": "sms_sent"})


class LoginConfirm(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code_in_cache = cache.get(f'otp_{serializer.validated_data["telephone"]}')

        print(code_in_cache, type(code_in_cache))
        print(
            serializer.validated_data["code"], type(serializer.validated_data["code"])
        )

        if code_in_cache != serializer.validated_data["code"]:
            return Response({"data": "wrong_code"})

        cache.delete(f'otp_{serializer.validated_data["telephone"]}')

        user, _ = User.objects.get_or_create(
            telephone=serializer.validated_data["telephone"], username=uuid.uuid4()
        )

        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user, token=generate_token())
        return Response({"token": token.token, "user_id": user.pk})
