from django import forms
from .models import (
    Article,
    Course,
    PracticeFile,
)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article       
        fields = ['title', 'course', 'text', ]

    def __init__(self, *args, **kwargs):
        owner_id = kwargs.pop('owner_id')
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(owner_id=owner_id)

class FileForm(forms.ModelForm):

    class Meta:
        model = PracticeFile       
        fields = ['title', 'course', 'file', ]

    def __init__(self, *args, **kwargs):
        owner_id = kwargs.pop('owner_id')
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(owner_id=owner_id)