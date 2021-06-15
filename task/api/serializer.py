from rest_framework import serializers
from .models import Student


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    
    def validate(self,data):
        email = data.get('student_email')
        if Student.objects.filter(student_email=email):
            raise serializers.ValidationError("Email already exist! Try with new email")
        return data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ["student_email","student_grade"]
        extra_kwargs = {'student_email':{'read_only':True},
                        'student_grade':{'read_only':True}}
        
        

