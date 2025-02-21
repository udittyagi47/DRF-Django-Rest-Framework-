from rest_framework import viewsets
from students.models import Student
from students.serializers import StudentSerializer  
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations on the Student model.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@api_view(['GET', 'POST'])
def student_list(request):
    """
    Handles listing all students (GET) and creating a new student (POST).
    """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def student_detail(request, pk):
    """
    Handles retrieving (GET), updating (PUT/PATCH), and deleting (DELETE) a single student.
    """
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)