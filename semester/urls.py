from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from semester.views import SemesterViews, SemesterDetailsViews


app_name='semester'

urlpatterns = [
    path('all/', SemesterViews.as_view()),
    path('single/<int:pk>/', SemesterDetailsViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
