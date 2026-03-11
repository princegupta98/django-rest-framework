from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')


urlpatterns = [
	# For Function Based Views
	path('students/', views.studentsView),
	path('student/<int:pk>/', views.studentDetailView),

	# For Class Based Views
	# path('employees/', views.Employees.as_view()),
	# path('employee/<int:pk>/', views.EmployeeDetail.as_view()),

	# For ViewSets
	path('', include(router.urls))
]