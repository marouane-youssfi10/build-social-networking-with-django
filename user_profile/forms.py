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
        self.fields['tag'].widget.attrs['id'] = 'tags'
        self.fields['tag'].widget.attrs['onclick'] = 'javascript:addEventListener("keydown", function (e) {if (this.value.length === 0 && e.which === 32) e.preventDefault(); });' \
                                                     ' addEventListener("keyup", () => {this.value = this.value.replace(/  +/g, " "); });'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'add tags, separated by commas. example: design, programmation, photographe, .....'
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
    photo_profile = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number', 'photo_profile')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs['onkeydown'] = 'javascript: return event.keyCode === 8 ||event.keyCode === 46 ? true : !isNaN(Number(event.key))'
        self.fields['first_name'].widget.attrs['onkeypress'] = 'javascript: return event.charCode != 32'
        self.fields['last_name'].widget.attrs['onkeypress'] = 'javascript: return event.charCode != 32'
        self.fields['first_name'].widget.attrs['onkeydown'] = 'javascript: return (event.keyCode!=188 && event.keyCode!=189 &&' \
                                                              '                    event.keyCode!=187 && event.keyCode!=191 &&' \
                                                              '                    event.keyCode!=221 && event.keyCode!=186 &&' \
                                                              '                    event.keyCode!=219 && event.keyCode!=226);'

        self.fields['last_name'].widget.attrs['onkeydown'] = 'javascript: return (event.keyCode!=188 && event.keyCode!=189 &&' \
                                                              '                    event.keyCode!=187 && event.keyCode!=191 &&' \
                                                              '                    event.keyCode!=221 && event.keyCode!=186 &&' \
                                                              '                    event.keyCode!=219 && event.keyCode!=226);'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    photo_cover = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = UserProfile
        fields = ('overview', 'title', 'photo_cover', 'education_title', 'education_year_start',
                  'education_year_end', 'education_description', 'location_country', 'location_city',
                  'hourly_work', 'type_work')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['overview'].widget = forms.Textarea(attrs={'rows': '5', 'cols': '5'})
        self.fields['education_description'].widget = forms.Textarea(attrs={'rows': '5', 'cols': '5'})

        self.fields['education_year_start'].widget.attrs['onkeydown'] = 'javascript: return event.keyCode === 8 ||event.keyCode === 46 ? true : !isNaN(Number(event.key))'
        self.fields['education_year_end'].widget.attrs['onkeydown'] = 'javascript: return event.keyCode === 8 ||event.keyCode === 46 ? true : !isNaN(Number(event.key))'

        self.fields['education_year_start'].widget.attrs['onKeyPress'] = 'if(this.value.length==4) return false'
        self.fields['education_year_end'].widget.attrs['onKeyPress'] = 'if(this.value.length==4) return false'

        self.fields['hourly_work'].widget.attrs['onkeydown'] = 'javascript: return event.keyCode === 8 ||event.keyCode === 46 ? true : !isNaN(Number(event.key))'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].required = False