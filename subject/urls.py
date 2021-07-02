from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from subject.views import SubjectViews, SubjectDetailsViews


app_name='subject'

urlpatterns = [
    path('all/', SubjectViews.as_view()),
    path('single/<int:pk>/', SubjectDetailsViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
