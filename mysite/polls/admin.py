from django.contrib import admin
from .models import Choice ,Question
# from .models import Choice
# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    
    # list_display = ('question_text', 'pub_date')
    # list_display = ('question_text', 'pub_date', 'was_published_recently')

    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines=[ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    search_fields = ['Choices_text']
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)


