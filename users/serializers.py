from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели платежей"""

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """Сериалайзер для модели Пользователь"""

    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
