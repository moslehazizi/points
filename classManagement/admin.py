from django.contrib import admin
from .models import Courses, Students

class CourseAdmin(admin.ModelAdmin):
    model = Courses
    list_display = ('name', 'desc',)

class CourseStudentAdmin(admin.ModelAdmin):
    model = Students
    list_display = ('course_name', 'first_name', 'last_name', 'national_id',)

admin.site.register(Courses, CourseAdmin)
admin.site.register(Students, CourseStudentAdmin)