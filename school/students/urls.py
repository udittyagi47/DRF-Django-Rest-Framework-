from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, student_list, student_detail




router = DefaultRouter()
router.register(r'students', StudentViewSet)  # DRF ViewSet

urlpatterns = [
    path('', include(router.urls)),  # Routes for ViewSet
    path('students/', student_list, name='student-list'),  # Function-based view for list
    path('students/<int:pk>/', student_detail, name='student-detail'),  # Function-based view for details
    
    
   
]


