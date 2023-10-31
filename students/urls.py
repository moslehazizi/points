from django.urls import path
from .views import (
    StudentTemplateView,
    StudentCourseListView,
    StudentCourseDetailView,
    StudentArticleListView,
    StudentArticelDetailView,
    StudentPresentDayListView,
    StudentPresentDayDetailView,
    StudentTestListView,
    StudentTestDetailView,
    StudentPracticeFileListView,
)

urlpatterns = [
    path('studentPage/', StudentTemplateView.as_view(), name='home_page'),
    path('courseListStudent/', StudentCourseListView.as_view(), name='sv_course_list'),
    path('courseDetailStudent/<uuid:pk>/', StudentCourseDetailView.as_view(), name='sv_course_detail'),
    path('articleListViewStudent/<uuid:pk>/articles/', StudentArticleListView.as_view(), name='sv_article_list'),
    path('articleDetailViewStudent/<uuid:pk>', StudentArticelDetailView.as_view(), name='sv_article_detail'),
    path('presentDayListViewStudent/<uuid:pk>/days/', StudentPresentDayListView.as_view(), name='sv_present_day'),
    path('presentDayDetailViewStudent/<uuid:pk>', StudentPresentDayDetailView.as_view(), name='sv_present_day_detail'),
    path('testListViewStudent/<uuid:pk>/tests/', StudentTestListView.as_view(), name='sv_test_list'),
    path('testDetailViewStudent/<uuid:pk>/', StudentTestDetailView.as_view(), name='sv_test_detail'),
    path('fileListViewStudent/<uuid:pk>/files', StudentPracticeFileListView.as_view(), name='sv_file_list'),
]
