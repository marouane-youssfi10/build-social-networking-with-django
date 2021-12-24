from django.contrib import admin
from .models import Ask_questions, TagsQuestions


class Ask_questionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'question', 'created_question', 'updated_question']

class TagsQuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'tags_user', 'tag']

admin.site.register(Ask_questions, Ask_questionsAdmin)
admin.site.register(TagsQuestions, TagsQuestionsAdmin)
