from django.urls import path
from student.views import stu_view

app_name = 'student'

urlpatterns = [
    path('.', stu_view, name='student')
]
