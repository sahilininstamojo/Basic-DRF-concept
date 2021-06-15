from functools import partial
from .serializer import AdminSerializer, StudentSerializer
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status, views
from rest_framework.response import Response



# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Admin_api(views.APIView):
    
    def get(self, request, email, *args, **kwargs):
        if email is not None:
            try:
                snippet = Student.objects.get(student_email=email)
                serializer = AdminSerializer(snippet)
                return Response(serializer.data)
            except:
                msg = {'msg':"Data not found!"}
                return Response(data=msg, status=status.HTTP_200_OK)
        snippet = Student.objects.all()
        serializer = AdminSerializer(snippet, many=True)
        return Response(data=serializer.data)
   
        
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = AdminSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            msg = {'msg':"Data created"}
            return Response(data=msg, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

        
    def put(self, request, *args, **kwarg):
        data = request.data
        pd = data.get('id')
        stu = Student.objects.get(id=pd)
        serializer = AdminSerializer(stu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':"Data updated"}
            return Response(data=msg)
        msg = {'msg':"Data not updated"}
        return Response(data=msg)
            
        
    def delete(self, request, email, *args, **kwargs):
        if Student.objects.filter(student_email=email):
            student_email = Student.objects.get(student_email=email)
            student_email.delete()
            msg = {'msg':"Data Deleted"}
            return Response(data=msg)
        msg = "No data found"
        return Response(data=msg)
        
    

@method_decorator(csrf_exempt, name='dispatch')
class Student_api(views.APIView):
    
    def get(self, request, email=None, *args, **kwargs):
        print(email)
        if email is not None:
            try:
                snippet = Student.objects.get(student_email=email)
                serializer = AdminSerializer(snippet)
                return Response(serializer.data)
            except:
                msg = {'msg':"Data not found!"}
                return Response(data=msg, status=status.HTTP_200_OK)
        msg = {'msg':"Welcome to Student portal"}
        return Response(data=msg, status=status.HTTP_200_OK)
    
    
    def put(self, request, *args, **kwarg):
        data = request.data
        pd = data.get('id')
        stu = Student.objects.get(id=pd)
        serializer = StudentSerializer(stu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':"Data updated"}
            return Response(data=msg)
        msg = {'msg':"Data not updated"}
        return Response(data=msg)
