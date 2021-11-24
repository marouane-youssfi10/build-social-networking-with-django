from django import forms
from accounts.models import Account, UserProfile, Experience_user, TagsUser, Social_media
from .models import PostProject, TagsProjects


class PostProjectForm(forms.ModelForm):
    class Meta:
        model = PostProject
        fields = ('name_project', 'type_work_project', 'location', 'start_price', 'end_price',
                  'description_project')

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
