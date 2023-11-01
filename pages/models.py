from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
import uuid
from django.shortcuts import render

User = settings.AUTH_USER_MODEL

class Person(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    person = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='person_to_user',
    )
    father_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField(null=True, blank=True)

    STUDENT = 1
    TEACHER = 10

    ROLE_CHOICES = (
        (STUDENT , 'Student') , (TEACHER , 'Teacher')
    )

    role = models.IntegerField(
        choices=ROLE_CHOICES,
        default=STUDENT
    )

class Course(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_to_user'
    )
    student = models.ManyToManyField(
        User,
        related_name='student_to_user',
    )
    resources = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class PracticeFile(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='files_to_course'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='file_to_owner',
    )
    file = models.FileField(upload_to='practices') 

    def __str__(self):
        return f'{self.title} _ {self.course} _ {self.file}'
    def get_absolute_url(self):
        return reverse('file_list')

class Article(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_to_user'
    )
    title = models.CharField(max_length=255,)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='article_to_course',
    )

    def __str__(self):
        return self.title
    
class Result(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='result_to_course',
    )
    date = models.DateField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='result_to_owner',
    )
    student_select = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='result_to_user')
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.date} _ {self.course} _ {self.student_select} : {self.result}'
    
class Test(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='test_to_course',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='test_to_owner',
    )
    result = models.ManyToManyField(
        Result,
        related_name='test_to_result',
    )

    def __str__(self):
        return f'{self.title} {self.course}'
    
class StudentPresent(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='student_present_to_course'
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_present_to_user',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_present_owner_to_user',
    )
    present = models.BooleanField(null=True, blank=True)
    day = models.DateField()

    def __str__(self):
        return f'{self.student} _ {self.present} _ {self.course} _ {self.day}'
    
class DayDate(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    day = models.DateField()
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="day_to_course",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_of_day_to_user',
    )
    present_state = models.ManyToManyField(
        StudentPresent,
        related_name='day_date_to_student_present',
    )

    def __str__(self):
        return f'{self.day} _ {self.course}'
    
class MessageBox(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    sender = models.ForeignKey(
        User,
        related_name='message_sender_to_user',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        related_name='message_receiver_to_user',
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=255)
    content = models.TextField()
    attachment = models.FileField(
        null=True,
        blank=True,
        upload_to='messages_attachments'
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver} about {self.subject} _ {self.date}'