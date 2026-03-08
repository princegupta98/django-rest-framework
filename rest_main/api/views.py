from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from students.models import Student
from .serializers import StudentSerializer


# Create your views here.
@api_view(["GET"])
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

