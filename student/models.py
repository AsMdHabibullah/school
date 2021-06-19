from teacher.models import Teacher
from django.db import models
from subject.models import Subject
from department.models import Department

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    depertment = models.OneToOneField(Department, on_delete=models.DO_NOTHING)
    # teacher= models.ForeignKey(Teacher)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
