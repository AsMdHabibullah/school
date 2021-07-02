# from django.db import models
# from django.db.models import fields
from rest_framework import serializers
from subject.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'details', 'teacher', 'department']
