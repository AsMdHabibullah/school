from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from semester.models import Semester
from rest_framework.response import Response
from semester.serializers import SemesterSerializer


# Create semester RestAPI views to use in frontand.
class SemesterViews(APIView):
    """
    List all semester, or create a new semester.
    """
    def get(self, request, format=None):
        try:
            semesters = Semester.objects.all()
            serializer = SemesterSerializer(semesters, many=True)
            # print(len(serializer.data))
            if len(serializer.data) > 0:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(data="semesters not found :(", status=status.HTTP_404_NOT_FOUND)
        except semesters.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = SemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# semester details also for update and destroy
class SemesterDetailsViews(APIView):
    """Single semester all method"""

    def get_semesters(self, pk):
        try:
            tec = Semester.objects.get(pk=pk)
            return tec
        except Semester.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # print(pk)
        semester = self.get_semesters(pk)
        return Response(semester, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        semester = self.get_semesters(pk)
        serializer = SemesterSerializer(semester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        semester = self.get_semesters(pk)
        if semester:
            semester.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
