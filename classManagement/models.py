import uuid
from django.db import models
from django.urls import reverse

class Courses(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])
    
class Students(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    course_name = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        related_name='student',
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=100)
    national_id = models.BigIntegerField()

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])