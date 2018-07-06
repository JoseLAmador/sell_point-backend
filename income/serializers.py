from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Income, Cliente


class IncomeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Income
        fields = '__all__'

class IncomeBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    incomes = IncomeBSerializer(
        many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'incomes')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'