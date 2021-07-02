from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from teacher.views import TeacherViews, TeacherDetailsViews


app_name='teacher'

urlpatterns = [
    path('all/', TeacherViews.as_view()),
    path('single/<int:pk>/', TeacherDetailsViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
