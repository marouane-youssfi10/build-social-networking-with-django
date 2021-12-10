from django import forms
from .models import CommentJobs, CommentProjects

class CommentProjectsForm(forms.ModelForm):
    class Meta:
        model = CommentProjects
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentProjectsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class CommentJobsForm(forms.ModelForm):
    class Meta:
        model = CommentJobs
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentJobsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'