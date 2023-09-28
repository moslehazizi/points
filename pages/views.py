from django.views import generic
from .models import Course
from django.http import HttpResponseRedirect

class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class CourseManagementTemplateView(generic.TemplateView):
    template_name = 'pages/courses_management.html'

class CourseCreateView(generic.CreateView):   

    model = Course
    fields = ['title', 'description',]
    template_name = 'pages/create_course.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

           
class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'pages/course_detail.html'
    
class CourseListView(generic.ListView):
    model = Course
    template_name = 'pages/course_list.html'
    context_object_name = 'courses'
    
    