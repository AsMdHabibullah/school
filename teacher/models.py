from django.db import models
from subject.models import Subject
from department.models import Department


# Create your models here.
class Teacher(models.Model):
    name= models.CharField(max_length=200)
    teacher_bio= models.TextField(max_length=5000)
    subject = models.ForeignKey(
        Subject,
        related_name="teacher",
        on_delete=models.DO_NOTHING
        )
    depertment = models.OneToOneField(
        Department,
        related_name="depertment", 
        on_delete=models.DO_NOTHING
        )

    def __str__(self):
        return self.name
