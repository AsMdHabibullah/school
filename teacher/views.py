from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from teacher.models import Teacher
from rest_framework.response import Response
from teacher.serializers import TeacherSerializer


# Create teacher RestAPI views to use in frontand.
class TeacherViews(APIView):
    """
    List all teacher, or create a new teacher.
    """

    def get(self, request, format=None):
        try:
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            # print(len(serializer.data))
            if len(serializer.data) > 0:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(data="teachers not found :(", status=status.HTTP_404_NOT_FOUND)
        except teachers.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# teacher details also for update and destroy
class TeacherDetailsViews(APIView):
    """Single teacher all method"""

    def get_teachers(self, pk):
        try:
            tec = Teacher.objects.get(pk=pk)
            return tec
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # print(pk)
        teacher = self.get_teachers(pk)
        return Response(teacher, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        teacher = self.get_teachers(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teacher = self.get_teachers(pk)
        if teacher:
            teacher.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
