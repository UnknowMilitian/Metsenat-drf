from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, telephone, password, **extra_fields):
        if not telephone:
            raise ValueError("Telephone is required")

        user = self.model(telephone=telephone, **extra_fields)
        user.password = make_password(password)
        # user.set_password(password)
        user.save()

        return user
