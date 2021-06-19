from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    dep_bio= models.TextField(max_length=10000, unique=True, blank=True)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
