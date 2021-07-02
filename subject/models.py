from django.db import models
from teacher.models import Teacher
from department.models import Department

# Create your models here.
class Subject(models.Model):
    name= models.CharField(max_length=200)
    details= models.TextField(max_length=5000)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.DO_NOTHING
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name
