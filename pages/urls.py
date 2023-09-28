from django.urls import path
from .views import (
    HomePageView,
    CourseManagementTemplateView,
    CourseCreateView,
    CourseDetailView,
    CourseListView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('courseManagement/', CourseManagementTemplateView.as_view(), name='courses_management'),
    path('courseCreate/', CourseCreateView.as_view(), name='create_course'),
    path('<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('coursesList/', CourseListView.as_view(), name='course_list'),
]
