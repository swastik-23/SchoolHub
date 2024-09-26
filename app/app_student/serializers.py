from rest_framework import serializers
from app.models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        extra_kwargsw = {'id':{'read_only':True},'password':{'write_only': True}}