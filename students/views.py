from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.conf import settings
from pages.models import (
    Course,
    Article,
    DayDate,
    Test,
    MessageBox
)


class StudentTemplateView(LoginRequiredMixin, generic.TemplateView):

    template_name = 'students/home_page.html'

class StudentCourseListView(LoginRequiredMixin, generic.ListView):
    
    model = Course
    context_object_name = "courses"
    template_name = 'students/sv_course_list.html'

    def get_queryset(self):
        return Course.objects.filter(student=self.request.user)
    
class StudentCourseDetailView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'students/sv_course_detail.html'

    def get_queryset(self):
        return Course.objects.filter(student=self.request.user)
    
class StudentArticleListView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'students/sv_article_list.html'

    def get_queryset(self):
        return Course.objects.filter(student=self.request.user)
    
class StudentArticelDetailView(LoginRequiredMixin, generic.DetailView):

    model = Article
    template_name = 'students/sv_article_detail.html'

class StudentPresentDayListView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'students/sv_present_day.html'

    def get_queryset(self):
        return Course.objects.filter(student=self.request.user)
    
class StudentPresentDayDetailView(LoginRequiredMixin, generic.DetailView):

    model = DayDate
    template_name = 'students/sv_present_day_detail.html'

class StudentTestListView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'students/sv_test_list.html'

    def get_queryset(self):
        return Course.objects.filter(student=self.request.user)
    
class StudentTestDetailView(LoginRequiredMixin, generic.DetailView):

    model = Test
    template_name = 'students/sv_test_detail.html'

class StudentPracticeFileListView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'students/sv_file_list.html'

    def get_queryset(self):
        return Course.objects.filter(student=self.request.user)
    
