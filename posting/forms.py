from django import forms
from .models import PostProject, TagsProjects, PostJobs, TagsJobs


class PostProjectForm(forms.ModelForm):
    class Meta:
        model = PostProject
        fields = '__all__'
        exclude = ['user', 'skills_tags_projects', 'viewers_project', 'updated_project', 'created_project', 'likes', 'hide']

    def __init__(self, *args, **kwargs):
        super(PostProjectForm, self).__init__(*args, **kwargs)
        self.fields['name_project'].widget.attrs['placeholder'] = 'Title project'
        self.fields['epic_coder'].widget.attrs['placeholder'] = 'Category: programming, Designer...'
        self.fields['location'].widget.attrs['placeholder'] = 'Country'
        self.fields['start_price'].widget.attrs['placeholder'] = 'Min Price'
        self.fields['end_price'].widget.attrs['placeholder'] = 'Max Price'
        self.fields['description_project'].widget.attrs['placeholder'] = 'Description'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True


class PostJobForm(forms.ModelForm):
    class Meta:
        model = PostJobs
        fields = '__all__'
        exclude = ['user', 'skills_tags_jobs', 'viewers_job', 'updated_job', 'created_job', 'likes', 'hide']

    def __init__(self, *args, **kwargs):
        super(PostJobForm, self).__init__(*args, **kwargs)
        self.fields['name_jobs'].widget.attrs['placeholder'] = 'Title Job'
        self.fields['type_work_job'].widget.attrs['placeholder'] = 'Full time, Part Time, Hourly'
        self.fields['epic_coder'].widget.attrs['placeholder'] = 'Category :Category: programming, Designer...'
        self.fields['location'].widget.attrs['placeholder'] = 'Country'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'
        self.fields['description_job'].widget.attrs['placeholder'] = 'Description'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True

class TagsProjectsForm(forms.ModelForm):
    class Meta:
        model = TagsProjects
        fields = ('tag',)

    def __init__(self, *args, **kwargs):
        super(TagsProjectsForm, self).__init__(*args, **kwargs)
        self.fields['tag'].widget.attrs['placeholder'] = 'Tags'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'add tags, separated by commas. example: design, programmation, photographe, .....'
            self.fields[field].required = True

class TagsJobForm(forms.ModelForm):
    class Meta:
        model = TagsJobs
        fields = ('tag',)

    def __init__(self, *args, **kwargs):
        super(TagsJobForm, self).__init__(*args, **kwargs)
        self.fields['tag'].widget.attrs['placeholder'] = 'Tags'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'add tags, separated by commas. example: design, programmation, photographe, .....'
            self.fields[field].required = True