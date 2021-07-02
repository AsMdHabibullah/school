# from django.db import models
# from django.db.models import fields
from rest_framework import serializers
from department.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields=['name', 'dep_bio']