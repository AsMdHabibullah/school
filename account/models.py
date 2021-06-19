from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=500)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    address_extra = models.CharField(max_length=200)
    user_bio= models.TextField(max_length=5000)
    user_img = models.ImageField(upload_to="static/images/user")

    def __str__(self):
        return f'${self.first_name} ${self.last_name}'