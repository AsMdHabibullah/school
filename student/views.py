from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from student.models import Student
from rest_framework.response import Response
from student.serializers import StudentSerializer


# Create department RestAPI views to use in frontand.
class StudentViews(APIView):
    """
    List all Department, or create a new department.
    """

    def get(self, request, format=None):
        try:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            # print(len(serializer.data))
            if len(serializer.data) > 0:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(data="Departments not found :(", status=status.HTTP_404_NOT_FOUND)
        except Student.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Department details also for update and destroy
class StudentDetailsViews(APIView):
    """Single department all method"""

    def get_students(self, pk):
        try:
            dep = Student.objects.get(pk=pk)
            return dep
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # print(pk)
        students = self.get_students(pk)
        return Response(students, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        student = self.get_department(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        students = self.get_students(pk)
        if students:
            students.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
