from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def studentsView(request):
	students = {
		'id':1,
		'name':'prince',
		'class':'CS'
	}
	# api endpoints dont return httpresponse, they return json/xml
	return JsonResponse(students)