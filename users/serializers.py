from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели платежей"""

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """Сериалайзер для модели Пользователь"""

    class Meta:
        model = User
        fields = "__all__"
