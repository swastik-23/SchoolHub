from rest_framework import serializers
from app.models import Classes

class ClassesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classes
        fields = ['id', 'name']
