from rest_framework import serializers

from .models import Payment, User


class UserDetailSerializer(serializers.ModelSerializer):
    payment = serializers.IntegerField()

    class Meta:
        model = User
        fields = (
            "id",
            "type_user" "fullname",
            "telephone",
            "payment",
            "company",
            "condition",
        )


class LoginConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    telephone = serializers.CharField(max_length=15)
