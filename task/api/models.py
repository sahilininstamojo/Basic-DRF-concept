from django.db import models
    
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_phone_number = models.CharField(max_length=10)
    student_grade = models.CharField(max_length=10)
    