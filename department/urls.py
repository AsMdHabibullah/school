from django.urls import path
from department.views import dep_view

app_name='department'

urlpatterns = [
    path('teacher/', dep_view, name='department')
]
