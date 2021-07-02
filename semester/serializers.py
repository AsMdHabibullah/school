# from django.db import models
# from django.db.models import fields
from rest_framework import serializers
from department.models import Department

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields = ('__all__')
