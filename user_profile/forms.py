from django import forms
from accounts.models import Account, UserProfile, Experience_user, TagsUser, Social_media


class ExperienceUserForm(forms.ModelForm):
    class Meta:
        model = Experience_user
        fields = ('experince_title', 'experince_description')

    def __init__(self, *args, **kwargs):
        super(ExperienceUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class TagsUserForm(forms.ModelForm):
    class Meta:
        model = TagsUser
        fields = ('tag',)

    def __init__(self, *args, **kwargs):
        super(TagsUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = Social_media
        fields = ('name', 'link')

    def __init__(self, *args, **kwargs):
        super(SocialMediaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = True

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    photo_profile = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)
    photo_cover = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('overview', 'title', 'photo_profile', 'photo_cover', 'education_title', 'education_year_start',
                  'education_year_end', 'education_description', 'location_country', 'location_city',
                  'hourly_work', 'type_work')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
