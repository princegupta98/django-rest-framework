from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from students.models import Student
from employees.models import Employee
from .serializers import EmployeeSerializer, StudentSerializer


# Create your views here.
# FUNCTION BASED VIEWS
@api_view(["GET", "POST"])
def studentsView(request):

    # Manual Serialization
    # students = Student.objects.all() #returns QuerySet type
    # students_list = list(students.values())

    # # api endpoints dont return httpresponse, they return json/xml
    # return JsonResponse(students_list, safe=False) #JsonResponse expects dict type, then we can pass 2nd param as false

    # USing DRF Serializer
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)  # student can be multiple

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, stattus=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeDetailView(APIView):
    pass