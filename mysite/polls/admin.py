from django.contrib import admin
from .models import Choice ,Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines=[ChoiceInline]          # makes choice editable
    list_filter = ['pub_date']
    search_fields = ['question_text']
    search_fields = ['Choices_text']
    
admin.site.register(Question, QuestionAdmin)



