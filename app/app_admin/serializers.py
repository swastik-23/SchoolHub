from rest_framework import serializers
from app.models import Admin

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'id': {'read_only': True}, 'password': {'write_only': True}}
