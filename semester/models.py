from django.db import models
from subject.models import Subject
from student.models import Student

# Create your models here.
class Semester(models.Model):
    name = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject)
    student = models.OneToOneField(Student, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
