import os
from django.views.generic import CreateView, DetailView, ListView
from .models import Courses, Students

class CoursesCreateView(CreateView):
    model = Courses
    template_name = 'classManagement/course_create.html'
    fields = ['name' , 'desc',]

class CourseListView(ListView):
    model = Courses
    template_name = 'classManagement/course_list.html'
    context_object_name = 'courses_item'

class CourseDetailView(DetailView):
    model = Courses
    template_name = 'classManagement/course_detail.html'

class StudentCreateView(CreateView):
    model = Students
    template_name = 'classManagement/student_create.html'
    fields = ['course_name', 'first_name', 'last_name', 'father_name', 'national_id',]

class StudentDetailView(DetailView):
    model = Students
    template_name = 'classManagement/student_detail.html'

class StudentDetailView(DetailView):
    model = Courses
    template_name = 'classManagement/student_list.html'