from django.urls import path

from . import views
urlpatterns = [
	# For Function Based Views
	path('students/', views.studentsView),
	path('student/<int:pk>/', views.studentDetailView),

	# For Class Based Views
	path('employees/', views.Employees.as_view()),
	path('employee/<int:pk>/', views.EmployeeDetail.as_view())
]