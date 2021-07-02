from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from department.views import DepatmentViews, DepartmentDetailsViews


app_name='department'

urlpatterns = [
    path('all/', DepatmentViews.as_view()),
    path('single/<int:pk>/', DepartmentDetailsViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
