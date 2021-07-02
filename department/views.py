from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from department.models import Department
from rest_framework.response import Response
from department.serializers import DepartmentSerializer


# Create department RestAPI views to use in frontand.
class DepatmentViews(APIView):
    """
    List all Department, or create a new department.
    """
    def get(self, request, format=None):
        try:
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            # print(len(serializer.data))
            if len(serializer.data) > 0:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(data="Departments not found :(", status=status.HTTP_404_NOT_FOUND)
        except Department.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Department details also for update and destroy
class DepartmentDetailsViews(APIView):
    """Single department all method"""
    def get_department(self, pk):
        try:
            dep = Department.objects.get(pk=pk)
            return dep
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # print(pk)
        department = self.get_department(pk)
        return Response(department, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        depertment = self.get_department(pk)
        serializer = DepartmentSerializer(depertment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        department = self.get_department(pk)
        if department:
            department.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
