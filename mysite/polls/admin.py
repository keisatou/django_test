"""This module is blha."""
from django.contrib import admin

from polls.models import Choice
from polls.models import Question


class ChoiceInline(admin.TabularInline):
    """ChoiceInline.

    description of ChoiceInline.
    """

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """QuestionAdmin.

    description of QuestionAdmin.
    """

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information',
         {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
