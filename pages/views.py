from typing import Any
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.conf import settings
from django.urls import reverse_lazy
from django.http import FileResponse, HttpRequest
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import (
    Course,
    Article,
    DayDate,
    StudentPresent,
    PracticeFile,
    Test,
    Result,
)
from .forms import ArticleForm, FileForm

User = settings.AUTH_USER_MODEL

class HomeTemplateView(generic.TemplateView):

    template_name = 'home.html'

class CoursesListView(LoginRequiredMixin, generic.ListView):
    
    model = Course
    context_object_name = "courses"
    template_name = 'pages/courses_list.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)
      
class CourseDetailView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'pages/course_detail.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user) 
    
class ArticleCreateView(LoginRequiredMixin, generic.CreateView):

    model = Article
    template_name = 'pages/article_create.html'
    form_class = ArticleForm

    def get_success_url(self):
        return self.request.GET.get('next')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)
    def get_form_kwargs(self):
        kwargs = super(ArticleCreateView, self).get_form_kwargs()
        kwargs.update({'owner_id': self.request.user})
        return kwargs
    
class ArticleListView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'pages/article_list.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)

class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):

    model = Article
    template_name = 'pages/article_update.html'
    fields = ('title', 'text', )

    def get_success_url(self):
        return self.request.GET.get('next')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user) 

class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):

    model = Article
    template_name = 'pages/article_delete.html'
    success_url = reverse_lazy('courses_list')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user) 

class ArticleDetailView(LoginRequiredMixin, generic.DetailView):

    model = Article
    template_name = 'pages/article_detail.html'

class DayPresentDetailView(LoginRequiredMixin, generic.DetailView):

    model = DayDate
    template_name = 'pages/day_detail.html'

    def get_queryset(self):
        return DayDate.objects.filter(owner=self.request.user)
    
class PresentUpdateView(LoginRequiredMixin, generic.UpdateView):

    model = StudentPresent
    template_name = 'pages/present_update.html'
    fields = ('student', 'present')

    def get_success_url(self):
        return self.request.GET.get('next')
        
    def get_queryset(self):
        return StudentPresent.objects.filter(owner=self.request.user)
    
class CourseDateListView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'pages/course_date_list.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)

class FileDetailView(LoginRequiredMixin, generic.DetailView):
    
    model = Course
    template_name = 'pages/file_view.html'

class FileCreateView(LoginRequiredMixin, generic.CreateView):

    model = PracticeFile
    template_name = 'pages/file_create.html'
    form_class = FileForm

    def get_success_url(self):
        return self.request.GET.get('next')
    def get_form_kwargs(self):
        kwargs = super(FileCreateView, self).get_form_kwargs()
        kwargs.update({'owner_id': self.request.user})
        return kwargs
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FileCreateView, self).form_valid(form)
    
class FileListView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'pages/file_list.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)
    
class FileUpdateView(LoginRequiredMixin, generic.UpdateView):

    model = PracticeFile
    template_name = 'pages/file_update.html'
    fields = ('title', 'course', 'file',)

    def get_success_url(self):
        return self.request.GET.get('next')
    
    def get_queryset(self):
        return PracticeFile.objects.filter(owner=self.request.user)
    
class FileDeleteView(LoginRequiredMixin, generic.DeleteView):

    model = PracticeFile
    template_name = 'pages/file_delete.html'
    success_url = reverse_lazy('courses_list')

    def get_queryset(self):
        return PracticeFile.objects.filter(owner=self.request.user) 

class PdfStudentListView(LoginRequiredMixin, generic.DetailView):

    model = Course

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        
        buffer = BytesIO()
        self = canvas.Canvas(buffer)
        cn = Course.name
        cs = Course.student
        self.drawString(100, 750, "List of students:")
        y = 700
        self.drawString(30, y, f'{cn}')
        self.drawString(30, y - 20, f'{cs}')
        y -= 60
    
        self.showPage()
        self.save()
    
        buffer.seek(0)

        response = FileResponse(buffer, 
                                as_attachment=True, 
                                filename='student_list.pdf')
        return response    
    
    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)

class StudentListView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'pages/student_list.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)
    
class TestTemplateView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'pages/test_view.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)

class TestListView(LoginRequiredMixin, generic.DetailView):

    model = Course
    template_name = 'pages/test_list.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)
    
class TestDetailView(LoginRequiredMixin, generic.DetailView):

    model = Test
    template_name = 'pages/test_detail.html'

    def get_queryset(self):
        return Test.objects.filter(owner=self.request.user)
    
class ResultUpdateView(LoginRequiredMixin, generic.UpdateView):

    model = Result
    template_name = 'pages/result_update.html'
    fields = ('result',)

    def get_success_url(self):
        return self.request.GET.get('next')
        
    def get_queryset(self):
        return Result.objects.filter(owner=self.request.user)
