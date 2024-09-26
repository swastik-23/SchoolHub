from rest_framework import serializers
from app.models import Account

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Account
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'id': {'read_only': True}, 'password': {'write_only': True}}