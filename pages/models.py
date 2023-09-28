from django.db import models
from django.conf import settings
from django.urls import reverse
 
User = settings.AUTH_USER_MODEL

class Course(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name= 'owner',
    )
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])
    
class Student(models.Model):
    course = models.ManyToManyField(
        Course,
        related_name='class_owner',
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    national_id = models.BigIntegerField()
    description = models.TextField()

