from rest_framework import serializers

from .models import Payment, User


class UserDetailSerializer(serializers.ModelSerializer):
    payment = serializers.IntegerField()

    class Meta:
        model = User
        fields = (
            "id",
            "type_user",
            "fullname",
            "telephone",
            "payment",
            "company",
            "condition",
        )
        read_only_fields = ("id",)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class LoginConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    telephone = serializers.CharField(max_length=15)
