from rest_framework import serializers
from app.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        extra_kwargs = {'id':{'read_only':True},'password':{'write_only':True}}
        