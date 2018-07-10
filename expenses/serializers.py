from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Provider
from income.serializers import UserSerializer

class ProviderSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=User.objects.all(),
                                                  allow_null=True, required=False)

    class Meta:
        model = Provider
        fields = '__all__'

    def create(self, validated_data):
        try:
            owner = validated_data.pop('owner_id')
        except:
            owner = None
        owner = Provider.objects.create(owner=owner, **validated_data)

        return owner

class EditProviderSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=User.objects.all(),
                                                      source='owner')
    class Meta:
        model = Provider
        fields = '__all__'
