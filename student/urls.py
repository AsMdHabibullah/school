from django.urls import path
from student.views import StudentViews, StudentDetailsViews

app_name = 'student'

urlpatterns = [
    path('all/', StudentViews.as_view()),
    path('single/<int:pk>/', StudentDetailsViews.as_view()),
]
