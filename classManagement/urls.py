from django.urls import path
from .views import (
    CoursesCreateView,
    CourseDetailView,
    CourseListView,
    StudentCreateView,
    StudentDetailView,
)

urlpatterns = [
    path('coursesCreate/', CoursesCreateView.as_view(), name='course_create'),
    path('coursesList/', CourseListView.as_view(), name='course_list'),
    path('course/<uuid:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/<uuid:pk>/studentCreate/', StudentCreateView.as_view(), name='student_create' ),
    path('studentCreate/<uuid:pk>/', StudentDetailView.as_view(), name='student_detail' ),
    path('studentList/<uuid:pk>/', StudentDetailView.as_view(), name='student_list'),
]

