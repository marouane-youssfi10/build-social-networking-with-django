from django import forms
from .models import PostProject, TagsProjects


class TagsProjectsForm(forms.ModelForm):
    class Meta:
        model = ['tag']
        fields = TagsProjects

    def __init__(self, *args, **kwargs):
        super(TagsProjectsForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs['placeholder'] = 'Tags'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True

class PostProjectForm(forms.ModelForm):
    class Meta:
        model = PostProject
        fields = '__all__'
        exclude = ['user', 'skills_tags_projects', 'updated_project', 'created_project']

    def __init__(self, *args, **kwargs):
        super(PostProjectForm, self).__init__(*args, **kwargs)
        self.fields['name_project'].widget.attrs['placeholder'] = 'Title project'
        self.fields['type_work_project'].widget.attrs['placeholder'] = 'Type Work'
        self.fields['location'].widget.attrs['placeholder'] = 'Country'
        self.fields['start_price'].widget.attrs['placeholder'] = 'Min Price'
        self.fields['end_price'].widget.attrs['placeholder'] = 'Max Price'
        self.fields['description_project'].widget.attrs['placeholder'] = 'Description'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True
