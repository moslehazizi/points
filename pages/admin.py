from django.contrib import admin
from .models import (
    Article,
    Course,
    Test,
    Result,
    DayDate,
    StudentPresent,
    PracticeFile,
    Person,
    MessageBox,
)

admin.site.register(Article)
admin.site.register(Course)
admin.site.register(Test)
admin.site.register(Result)
admin.site.register(DayDate)
admin.site.register(StudentPresent)
admin.site.register(PracticeFile)
admin.site.register(Person)
admin.site.register(MessageBox)