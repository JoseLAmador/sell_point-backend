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
    #incomes = IncomeBSerializer(
     #   many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username')#, 'incomes')


class ClienteSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=User.objects.all(),
                                                 allow_null=True, required=False)

    class Meta:
        model = Cliente
        fields = '__all__'

    def create(self, validated_data):
        try:
            owner = validated_data.pop('owner_id')
        except:
            owner = None


        owner = Cliente.objects.create(owner=owner, **validated_data)

        return owner

class EditClienteSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=User.objects.all(),
                                                  source='owner')

    class Meta:
        model = Cliente
        fields = '__all__'