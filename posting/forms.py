from django import forms
from .models import PostProject, TagsProjects


class PostProjectForm(forms.ModelForm):
    class Meta:
        model = PostProject
        fields = '__all__'
        exclude = ['user', 'skills_tags_projects', 'updated_project', 'created_project', 'likes']

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
