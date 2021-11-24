from django import forms
from accounts.models import Account, UserProfile, Experience_user, TagsUser, Social_media
from .models import PostProject, TagsProjects


class ExperienceUserForm(forms.ModelForm):
    class Meta:
        model = PostProject
        fields = ('name_project', 'type_work_project', 'location', 'start_price', 'end_price',
                  'description_project')

    def __init__(self, *args, **kwargs):
        super(ExperienceUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True
